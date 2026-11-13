#!/usr/bin/env python3
# sync-mcp-distribute - Distribute MCP server definitions to all agent configs
# Usage: sync-mcp-distribute.py [server_name]
#   no arg -> distribute all servers
#   arg    -> distribute only that server

import json
import os
import re
import sys

REPO_DIR = "/home/perez/projetos/ai-tools"
INPUT_FILE = os.path.join(REPO_DIR, "mcp", "servers.json")

def load_servers():
    with open(INPUT_FILE, "r") as f:
        return json.load(f)

def filter_server(servers, name):
    if name:
        return {name: servers[name]} if name in servers else {}
    return servers

def distribute_opencode(servers):
    path = os.path.expanduser("~/.config/opencode/opencode.jsonc")
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        return False
    
    with open(path, "r") as f:
        content = f.read()
    
    try:
        import json5
        data = json5.loads(content)
    except ImportError:
        content = re.sub(r"//.*", "", content)
        content = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
        data = json.loads(content)
    
    if "mcp" not in data:
        data["mcp"] = {}
    
    for name, config in servers.items():
        if "url" not in config and "command" not in config:
            continue
        mcp_config = {
            "type": config.get("type", "remote"),
            "enabled": config.get("enabled", True),
            "source": "opencode",
        }
        if "headers" in config:
            mcp_config["headers"] = config["headers"]
        if "oauth" in config:
            mcp_config["oauth"] = config["oauth"]
        data["mcp"][name] = mcp_config
    
    try:
        import json5
        output = json5.dumps(data, indent=2, quote_keys=True)
    except ImportError:
        output = json.dumps(data, indent=2)
    
    with open(path, "w") as f:
        f.write(output)
    
    print(f"Updated opencode: {path}")
    return True

def distribute_claude(servers):
    path = os.path.expanduser("~/.claude.json")
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        return False
    
    with open(path, "r") as f:
        data = json.load(f)
    
    if "mcpServers" not in data:
        data["mcpServers"] = {}
    
    for name, config in servers.items():
        if "url" not in config:
            continue
        mcp_config = {
            "type": config.get("type", "http"),
            "url": config["url"],
        }
        if "headers" in config:
            mcp_config["headers"] = config["headers"]
        if "oauth" in config:
            mcp_config["oauth"] = config["oauth"]
        data["mcpServers"][name] = mcp_config
    
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated claude: {path}")
    return True

def distribute_codex(servers):
    path = os.path.expanduser("~/.codex/config.toml")
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        return False
    
    with open(path, "r") as f:
        content = f.read()
    
    existing_servers = set()
    for match in re.finditer(r"\[mcp_servers\.([^.\]]+)\]", content):
        existing_servers.add(match.group(1))
    
    servers_to_add = {
        name: config
        for name, config in servers.items()
        if ("url" in config or "command" in config) and name not in existing_servers
    }
    
    if not servers_to_add:
        print(f"Codex: no new servers to add")
        return True
    
    lines = content.split("\n")
    last_mcp_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("[mcp_servers"):
            last_mcp_idx = i
    
    if last_mcp_idx < 0:
        new_lines = lines + [""]
        for name, config in servers_to_add.items():
            new_lines.append(f"[mcp_servers.{name}]")
            if "url" in config:
                new_lines.append(f'url = "{config["url"]}"')
            if "command" in config:
                new_lines.append(f'command = "{config["command"]}"')
            if "args" in config:
                new_lines.append(f"args = {json.dumps(config['args'])}")
            if "type" in config:
                new_lines.append(f'type = "{config["type"]}"')
            if "bearer_token_env_var" in config:
                new_lines.append(
                    f'bearer_token_env_var = "{config["bearer_token_env_var"]}"'
                )
    else:
        new_lines = lines[: last_mcp_idx + 1]
        for name, config in servers_to_add.items():
            new_lines.append(f"[mcp_servers.{name}]")
            if "url" in config:
                new_lines.append(f'url = "{config["url"]}"')
            if "command" in config:
                new_lines.append(f'command = "{config["command"]}"')
            if "args" in config:
                new_lines.append(f"args = {json.dumps(config['args'])}")
            if "type" in config:
                new_lines.append(f'type = "{config["type"]}"')
            if "bearer_token_env_var" in config:
                new_lines.append(
                    f'bearer_token_env_var = "{config["bearer_token_env_var"]}"'
                )
        new_lines.extend(lines[last_mcp_idx + 1:])
    
    with open(path, "w") as f:
        f.write("\n".join(new_lines))
    
    added = ", ".join(servers_to_add.keys())
    print(f"Updated codex: {path} (added: {added})")
    return True

def main():
    server_name = sys.argv[1] if len(sys.argv) > 1 else None
    servers = filter_server(load_servers(), server_name)
    
    print("Distributing MCP servers to all agents...")
    
    distribute_opencode(servers)
    distribute_claude(servers)
    distribute_codex(servers)
    
    print("\nDistribution complete!")

if __name__ == "__main__":
    main()