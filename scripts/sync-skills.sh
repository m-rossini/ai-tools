#!/bin/bash
# sync-skills - Sync skill directories to Claude, Codex, and OpenCode
# Usage: sync-skills.sh [skill_name]
#   no arg  -> sync all skills
#   arg     -> sync only that skill

REPO_SKILLS_DIR="/home/perez/projetos/ai-tools/skills"
if [ ! -d "$REPO_SKILLS_DIR" ]; then
  echo "Error: Repository skills directory not found at $REPO_SKILLS_DIR"
  exit 1
fi

REPO_SKILLS_REAL=$(realpath "$REPO_SKILLS_DIR")

CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CODEX_SKILLS_DIR="$HOME/.codex/skills"
OPENCODE_SKILLS_DIR="$HOME/.config/opencode/skills"

AGENT_REPO="$REPO_SKILLS_DIR/AGENT.md"

# Link AGENT.md into an agent's skills dir, unless that dir already resolves
# back to the repo (in which case the repo is already mounted there).
link_agent_md() {
  local agent_dir="$1"
  local agent_dir_real
  agent_dir_real=$(realpath "$agent_dir" 2>/dev/null)

  if [ "$agent_dir_real" = "$REPO_SKILLS_REAL" ]; then
    echo "  $agent_dir is a link to the repo itself; AGENT.md already present"
    return 0
  fi

  mkdir -p "$agent_dir" || return 1
  local agent_link="$agent_dir/AGENT.md"
  if [ -L "$agent_link" ]; then
    if [ "$(readlink "$agent_link")" != "$AGENT_REPO" ]; then
      rm -f "$agent_link"
      ln -sf "$AGENT_REPO" "$agent_link"
      echo "  Repointed $agent_link"
    fi
  elif [ -e "$agent_link" ]; then
    echo "  Warning: $agent_link exists and is not a symlink; skipping"
  else
    ln -sf "$AGENT_REPO" "$agent_link"
    echo "  Linked $agent_link"
  fi
}

# Symlink a single skill into one agent dir.
# Skips when the destination would be the source itself.
sync_skill_into() {
  local skill_dir="$1"
  local skill_name="$2"
  local agent_dir="$3"
  local agent_dir_real
  agent_dir_real=$(realpath "$agent_dir" 2>/dev/null)

  # Destination already resolves to the repo: nothing to link.
  if [ "$agent_dir_real" = "$REPO_SKILLS_REAL" ]; then
    return 0
  fi

  mkdir -p "$agent_dir" || return 1
  local dst="$agent_dir/$skill_name"

  # Never let a link point at itself.
  if [ "$(realpath "$dst" 2>/dev/null)" = "$(realpath "$skill_dir")" ] && [ -L "$dst" ]; then
    return 0
  fi

  if [ -L "$dst" ]; then
    if [ "$(readlink "$dst")" != "$skill_dir" ]; then
      rm -f "$dst"
      ln -s "$skill_dir" "$dst"
    fi
  elif [ -e "$dst" ]; then
    echo "  Warning: $dst exists and is not a symlink; skipping"
    return 1
  else
    ln -s "$skill_dir" "$dst"
  fi
}

sync_skill() {
  local skill_dir="$1"
  local skill_name="$2"
  local agent_dirs=()

  for d in "$CLAUDE_SKILLS_DIR" "$CODEX_SKILLS_DIR" "$OPENCODE_SKILLS_DIR"; do
    local d_real
    d_real=$(realpath "$d" 2>/dev/null)
    [ "$d_real" = "$REPO_SKILLS_REAL" ] && continue
    agent_dirs+=("$d")
  done

  if [ ${#agent_dirs[@]} -eq 0 ]; then
    echo "  Skill '$skill_name' already lives in the repo, which every agent links to."
    return 0
  fi

  for d in "${agent_dirs[@]}"; do
    sync_skill_into "$skill_dir" "$skill_name" "$d" || true
  done
  echo "  Synced skill '$skill_name' -> ${#agent_dirs[@]} agent dir(s)"
}

link_agent_md "$CLAUDE_SKILLS_DIR"
link_agent_md "$CODEX_SKILLS_DIR"
link_agent_md "$OPENCODE_SKILLS_DIR"

if [ -n "$1" ]; then
  skill_dir="$REPO_SKILLS_DIR/$1"
  if [ ! -d "$skill_dir" ]; then
    echo "Error: skill '$1' not found in $REPO_SKILLS_DIR"
    exit 1
  fi
  sync_skill "$skill_dir" "$1"
  exit 0
fi

for skill_dir in "$REPO_SKILLS_DIR"/*; do
  [ -d "$skill_dir" ] || continue
  skill_name=$(basename "$skill_dir")
  [ "$skill_name" = "AGENT.md" ] && continue
  [[ "$skill_name" == .* ]] && continue
  sync_skill "$skill_dir" "$skill_name"
done

echo "Skills sync complete."