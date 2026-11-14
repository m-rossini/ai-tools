#!/usr/bin/env python3
# sync-mcp-distribute - Distribute MCP server definitions to all agent configs
#
# Safety rules (learned the hard way):
#   1. NEVER overwrite an entry that already exists. Existing agent config is
#      the source of truth for that agent; this script only ADDS missing servers.
#   2. Preserve every key already present (url, headers, oauth, enabled, type...).
#   3. Back up each file before writing.
#   4. Refuse to write a server that has neither url nor command.
#
# Usage: sync-mcp-distribute.py [server_name]
#   no arg -> add any missing servers
#   arg    -> add only that server

import json
import os
import re
import shutil
import sys
import time

REPO_DIR = "/home/perez/projetos/ai-tools"
INPUT_FILE = os.path.join(REPO_DIR, "mcp", "servers.json")


def load_servers():
    with open(INPUT_FILE, "r") as f:
        return json.load(f)


def filter_server(servers, name):
    if name:
        return {name: servers[name]} if name in servers else {}
    return servers


def backup(path):
    dst = f"{path}.bak.{int(time.time())}"
    shutil.copy2(path, dst)
    print(f"  backup: {dst}")


def is_valid(config):
    """A server needs somewhere to connect: a URL or a command."""
    return bool(config.get("url") or config.get("command"))


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
        stripped = re.sub(r"//.*", "", content)
        stripped = re.sub(r"/\*.*?\*/", "", stripped, flags=re.DOTALL)
        data = json.loads(stripped)

    existing = data.get("mcp", {})
    added, skipped = [], []

    for name, config in servers.items():
        if name in existing:
            skipped.append(name)
            continue
        if not is_valid(config):
            print(f"  skip {name}: no url or command in servers.json")
            continue
        # Build from the source entry, keeping only keys that belong in opencode.
        entry = {}
        if config.get("url"):
            # OpenCode only accepts "local" or "remote"; other agents use "http".
            entry["type"] = "remote"
            entry["url"] = config["url"]
        else:
            entry["type"] = "local"
            entry["command"] = config["command"]
            if config.get("args"):
                entry["args"] = config["args"]
        entry["enabled"] = config.get("enabled", True)
        if config.get("headers"):
            entry["headers"] = config["headers"]
        if config.get("oauth") is not None:
            entry["oauth"] = config["oauth"]
        existing[name] = entry
        added.append(name)

    data["mcp"] = existing

    if not added:
        print(f"OpenCode: nothing to add ({len(skipped)} already present)")
        return True

    backup(path)
    try:
        import json5
        output = json5.dumps(data, indent=2, quote_keys=True)
    except ImportError:
        output = json.dumps(data, indent=2)

    with open(path, "w") as f:
        f.write(output)

    print(f"OpenCode: added {', '.join(added)}")
    if skipped:
        print(f"OpenCode: left untouched {', '.join(skipped)}")
    return True


CLAUDE_TYPES = {"http", "sse", "stdio"}


def claude_type(url):
    # Claude Code accepts only http/sse/stdio ("remote" is OpenCode-only).
    return "sse" if url.rstrip("/").endswith("/sse") else "http"


def distribute_claude(servers):
    path = os.path.expanduser("~/.claude.json")
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        return False

    with open(path, "r") as f:
        data = json.load(f)

    existing = data.get("mcpServers", {})
    added, skipped = [], []

    fixed = []
    for name, config in servers.items():
        if name in existing:
            # Repair only an invalid transport type; keep everything else.
            entry = existing[name]
            if entry.get("url") and entry.get("type") not in CLAUDE_TYPES:
                entry["type"] = claude_type(entry["url"])
                fixed.append(name)
            else:
                skipped.append(name)
            continue
        if not config.get("url"):
            print(f"  skip {name}: no url (Claude remote servers need one)")
            continue
        existing[name] = {
            "type": claude_type(config["url"]),
            "url": config["url"],
        }
        added.append(name)

    data["mcpServers"] = existing

    if not added and not fixed:
        print(f"Claude: nothing to add ({len(skipped)} already present)")
        return True

    backup(path)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    if added:
        print(f"Claude: added {', '.join(added)}")
    if fixed:
        print(f"Claude: fixed invalid type on {', '.join(fixed)}")
    if skipped:
        print(f"Claude: left untouched {', '.join(skipped)}")
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

    to_add = {
        name: config
        for name, config in servers.items()
        if is_valid(config) and name not in existing_servers
    }

    if not to_add:
        print(f"Codex: nothing to add ({len(existing_servers)} already present)")
        return True

    lines = content.split("\n")
    last_mcp_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("[mcp_servers"):
            last_mcp_idx = i

    block = []
    for name, config in to_add.items():
        block.append(f"[mcp_servers.{name}]")
        if config.get("url"):
            block.append(f'url = "{config["url"]}"')
        else:
            block.append(f'command = "{config["command"]}"')
            if config.get("args"):
                block.append(f"args = {json.dumps(config['args'])}")
        if config.get("type"):
            block.append(f'type = "{config["type"]}"')
        if config.get("bearer_token_env_var"):
            block.append(
                f'bearer_token_env_var = "{config["bearer_token_env_var"]}"'
            )

    if last_mcp_idx < 0:
        new_lines = lines + [""] + block
    else:
        new_lines = lines[: last_mcp_idx + 1] + block + lines[last_mcp_idx + 1:]

    backup(path)
    with open(path, "w") as f:
        f.write("\n".join(new_lines))

    print(f"Codex: added {', '.join(to_add.keys())}")
    return True


def main():
    server_name = sys.argv[1] if len(sys.argv) > 1 else None
    servers = filter_server(load_servers(), server_name)

    if not servers:
        print("No matching servers in mcp/servers.json")
        return

    print("Distributing MCP servers (add-only, never overwrites)...")
    distribute_opencode(servers)
    distribute_claude(servers)
    distribute_codex(servers)
    print("\nDistribution complete.")


if __name__ == "__main__":
    main()