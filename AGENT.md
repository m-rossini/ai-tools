# Global Claude Instructions & Skill Trigger Guide

You have access to local skills stored in `~/.claude/skills/`. Use this guide to determine when to trigger them contextually:

## 1. Multi-Agent Synchronization (`agent-coordination`)
- **Path:** `~/.claude/skills/agent-coordination/`
- **When to trigger:** Use when working in a repository where multiple AI CLI agents (Claude, Codex, Gemini, etc.) are working concurrently in separate Git worktrees.
- **Behavior:** Check for `COLLABORATION.md` at the project root, use it as an ephemeral scratchpad, prune resolved entries, and record permanent architectural decisions in Jira if available. Ignore if working alone.

## 2. Concise Writing (`concise-writing`)
- **Path:** `~/.claude/skills/concise-writing/`
- **When to trigger:** Use when the user requests direct, punchy, low-fluff answers, status reports, or summaries without conversational filler.

## 3. Container Testing (`container-test`)
- **Path:** `~/.claude/skills/container-test/`
- **When to trigger:** Use when setting up, running, or debugging containerized environments (Docker/Podman) or executing test suites.

## 4. Git Workflows (`git`)
- **Path:** `~/.claude/skills/git/`
- **When to trigger:** Use when managing complex git operations, branch strategies, worktrees, or resolving merge states.