#!/usr/bin/env python3
# sync-mcp-remove - Remove an MCP server from mcp/servers.json and all agent configs
#
# Usage: sync-mcp-remove.py <server_name>
#
# Backs up each file before writing. Reports what it could not find.

import json
import os
import re
import shutil
import sys
import time

REPO_DIR = "/home/perez/projetos/ai-tools"
SERVERS_FILE = os.path.join(REPO_DIR, "mcp", "servers.json")

OPENCODE_CONFIG = os.path.expanduser("~/.config/opencode/opencode.jsonc")
CLAUDE_CONFIG = os.path.expanduser("~/.claude.json")
CODEX_CONFIG = os.path.expanduser("~/.codex/config.toml")


def backup(path):
    dst = f"{path}.bak.{int(time.time())}"
    shutil.copy2(path, dst)
    print(f"  backup: {dst}")


def remove_from_servers_file(name):
    if not os.path.exists(SERVERS_FILE):
        print(f"  servers.json: not found")
        return
    with open(SERVERS_FILE, "r") as f:
        data = json.load(f)
    if name not in data:
        print(f"  servers.json: '{name}' not present")
        return
    data.pop(name)
    with open(SERVERS_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  servers.json: removed '{name}'")


def remove_from_opencode(name):
    if not os.path.exists(OPENCODE_CONFIG):
        print(f"  opencode: config not found")
        return
    import json5
    with open(OPENCODE_CONFIG, "r") as f:
        data = json5.load(f)
    mcp = data.get("mcp", {})
    if name not in mcp:
        print(f"  opencode: '{name}' not present")
        return
    mcp.pop(name)
    backup(OPENCODE_CONFIG)
    with open(OPENCODE_CONFIG, "w") as f:
        f.write(json5.dumps(data, indent=2, quote_keys=True))
    print(f"  opencode: removed '{name}'")


def remove_from_claude(name):
    if not os.path.exists(CLAUDE_CONFIG):
        print(f"  claude: config not found")
        return
    with open(CLAUDE_CONFIG, "r") as f:
        data = json.load(f)
    mcp = data.get("mcpServers", {})
    if name not in mcp:
        print(f"  claude: '{name}' not present")
        return
    mcp.pop(name)
    backup(CLAUDE_CONFIG)
    with open(CLAUDE_CONFIG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  claude: removed '{name}'")


def remove_from_codex(name):
    """Drop [mcp_servers.<name>] and any [mcp_servers.<name>.*] subsections."""
    if not os.path.exists(CODEX_CONFIG):
        print(f"  codex: config not found")
        return

    with open(CODEX_CONFIG, "r") as f:
        lines = f.read().split("\n")

    # Section header for the server itself, or any of its tool subsections.
    target = re.compile(
        r"^\[mcp_servers\." + re.escape(name) + r"(\.[^\]]+)?\]\s*$"
    )

    kept = []
    removed_sections = 0
    skipping = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("["):
            if target.match(stripped):
                skipping = True
                removed_sections += 1
                continue
            skipping = False
        if skipping:
            continue
        kept.append(line)

    if removed_sections == 0:
        print(f"  codex: '{name}' not present")
        return

    # Collapse runs of blank lines left behind by removed sections.
    cleaned = []
    for line in kept:
        if line.strip() == "" and cleaned and cleaned[-1].strip() == "":
            continue
        cleaned.append(line)

    backup(CODEX_CONFIG)
    with open(CODEX_CONFIG, "w") as f:
        f.write("\n".join(cleaned))
    print(f"  codex: removed '{name}' ({removed_sections} section(s))")


def main():
    if len(sys.argv) < 2:
        print("Usage: sync-mcp-remove.py <server_name>")
        sys.exit(1)

    name = sys.argv[1]

    print(f"Removing MCP server '{name}' everywhere...")
    remove_from_servers_file(name)
    remove_from_opencode(name)
    remove_from_claude(name)
    remove_from_codex(name)
    print("\nDone.")


if __name__ == "__main__":
    main()