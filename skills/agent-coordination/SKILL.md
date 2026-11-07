---
name: agent-coordination
description: Optional lightweight multi-agent synchronization protocol for CLI agents (Claude, Codex, Gemini, etc.) working in parallel Git worktrees. Uses an ephemeral COLLABORATION.md scratchpad for real-time coordination and prunes resolved entries. Use when multiple AI tools work concurrently on the same project repository.
---

# Multi-Agent Worktree Synchronization Protocol

This skill governs coordination when multiple AI CLI agents work simultaneously in separate Git worktrees on the same repository. **This skill is optional**—if you are the only active agent or no other worktrees are in progress, skip these steps.

## 1. Discovery & Activation
* Check if `COLLABORATION.md` exists at the root of the repository. 
* If it **does not exist**, and you are working alone, do nothing.
* If it **exists**, read it at the start of your session to align with concurrent worktrees.

## 2. Ephemeral Scratchpad Rules (`COLLABORATION.md`)
`COLLABORATION.md` is a **volatile bulletin board**, not a permanent log. It must never grow indefinitely.

* **Format for Notes:** See [examples.md](./examples.md) for concrete message formatting.
* **The Pruning Rule:** Once a question is answered, a request is fulfilled, or your task is completed, **delete your entries** from `COLLABORATION.md`.

## 3. Permanence & Fallback (Jira Integration)
* **If Jira is available in the project:**
  * Tactical Q&A history $\rightarrow$ Log as a comment on the Jira ticket.
  * Structural changes/decisions $\rightarrow$ Update the Jira ticket description.
* **If Jira is NOT available:**
  * Simply prune the resolved items from `COLLABORATION.md`. The loss of permanent history is fully expected and acceptable.

## Reference Examples
For concrete formatting of notes, targeted routing, and pruning workflows, see [examples.md](./examples.md).