#!/usr/bin/env python3
# sync-mcp-collect - Collect MCP server definitions from all agent configs

import json
import os
import re
import sys

REPO_DIR = "/home/perez/projetos/ai-tools"
OUTPUT_FILE = os.path.join(REPO_DIR, "mcp", "servers.json")

BEARER_ENV_MAP = {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "github",
    "RENDER_API_KEY": "render",
}

def redact_bearer(headers, server_name):
    """Replace literal bearer tokens with {env:VAR} references"""
    redacted = {}
    for k, v in (headers or {}).items():
        mv = re.match(r'^Bearer\s+(\S+)$', v or '')
        if mv:
            token = mv.group(1)
            env_var = f"{server_name.upper()}_TOKEN"
            # Try to find a known mapping
            for ev, sn in BEARER_ENV_MAP.items():
                if sn == server_name:
                    env_var = ev
            redacted[k] = f"Bearer {{env:{env_var}}}"
        else:
            redacted[k] = v
    return redacted

def read_opencode_mcp():
    path = os.path.expanduser("~/.config/opencode/opencode.jsonc")
    servers = {}
    if not os.path.exists(path):
        return servers
    try:
        import json5
        with open(path, 'r') as f:
            content = f.read()
        data = json5.loads(content)
        mcp = data.get('mcp', {})
        for name, config in mcp.items():
            if isinstance(config, dict):
                entry = {'source': 'opencode', 'enabled': config.get('enabled', True)}
                url = config.get('url')
                if url:
                    entry['url'] = url
                    entry['type'] = config.get('type', 'remote')
                if 'headers' in config:
                    entry['headers'] = redact_bearer(config['headers'], name)
                if 'oauth' in config:
                    entry['oauth'] = config['oauth']
                servers[name] = entry
    except Exception as e:
        print(f"Error reading opencode config: {e}", file=sys.stderr)
    return servers

def read_claude_mcp():
    path = os.path.expanduser("~/.claude.json")
    servers = {}
    if not os.path.exists(path):
        return servers
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        mcp = data.get('mcpServers', {})
        for name, config in mcp.items():
            entry = {'source': 'claude', 'enabled': True}
            url = config.get('url')
            if url:
                entry['url'] = url
                entry['type'] = config.get('type', 'http')
            if 'headers' in config:
                entry['headers'] = redact_bearer(config['headers'], name)
            if 'oauth' in config:
                entry['oauth'] = config['oauth']
            servers[name] = entry
    except Exception as e:
        print(f"Error reading claude config: {e}", file=sys.stderr)
    return servers

def read_codex_mcp():
    path = os.path.expanduser("~/.codex/config.toml")
    servers = {}
    if not os.path.exists(path):
        return servers
    try:
        with open(path, 'r') as f:
            content = f.read()
        current_server = None
        for line in content.split('\n'):
            stripped = line.strip()
            m = re.match(r'\[mcp_servers\.([^.\]]+)\]', stripped)
            if m:
                current_server = m.group(1)
                servers[current_server] = {'source': 'codex', 'enabled': True}
                continue
            if re.match(r'\[mcp_servers\..*\..*\]', stripped):
                current_server = None
                continue
            if current_server is None:
                continue
            m = re.match(r'url\s*=\s*"([^"]+)"', stripped)
            if m:
                servers[current_server]['url'] = m.group(1)
                continue
            m = re.match(r'type\s*=\s*"([^"]+)"', stripped)
            if m:
                servers[current_server]['type'] = m.group(1)
                continue
            m = re.match(r'command\s*=\s*"([^"]+)"', stripped)
            if m:
                servers[current_server]['command'] = m.group(1)
                continue
            m = re.match(r'bearer_token_env_var\s*=\s*"([^"]+)"', stripped)
            if m:
                servers[current_server]['bearer_token_env_var'] = m.group(1)
                continue
            m = re.match(r'args\s*=\s*(\[[^\]]*\])', stripped)
            if m:
                try:
                    servers[current_server]['args'] = json.loads(m.group(1))
                except json.JSONDecodeError:
                    servers[current_server]['args'] = []
                continue
    except Exception as e:
        print(f"Error reading codex config: {e}", file=sys.stderr)
    return servers

def main():
    all_servers = {}
    sources = [
        ('opencode', read_opencode_mcp()),
        ('claude', read_claude_mcp()),
        ('codex', read_codex_mcp()),
    ]
    for source_name, servers in sources:
        for name, config in servers.items():
            if name not in all_servers:
                all_servers[name] = config
            else:
                existing = all_servers[name]
                existing['sources'] = existing.get('sources', [existing['source']])
                if source_name not in existing['sources']:
                    existing['sources'].append(source_name)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_servers, f, indent=2)
    print(f"Collected {len(all_servers)} MCP servers:")
    for name, config in sorted(all_servers.items()):
        sources_str = ', '.join(config.get('sources', [config.get('source')]))
        url = config.get('url', config.get('command', 'n/a'))
        print(f"  {name}: {url} (from {sources_str})")
    print(f"\nSaved to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()