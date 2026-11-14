---
name: agent-coordination
description: Optional lightweight multi-agent synchronization protocol for CLI agents (Claude, Codex, Gemini, etc.) working in parallel Git worktrees. Uses an ephemeral COLLABORATION.md scratchpad for real-time coordination and prunes resolved entries. Use when multiple AI tools work concurrently on the same project repository.
---

# Multi-Agent Worktree Synchronization Protocol

This skill governs coordination when multiple AI CLI agents work simultaneously in separate Git worktrees on the same repository. **This skill is optional**—if you are the only active agent or no other worktrees are in progress, skip these steps.

## 1. Discovery & Activation
* Check if `COLLABORATION.md` exists at the root of the repository. If not create one.
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

## 4. Owner To-Do, Status and Hygiene (applies to EVERY participant, the coordinator included)
The owner reads the board, not the agents' chats. Communicate proactively.

* **Owner To-Do list:** `COLLABORATION.md` opens with an `OWNER TO-DO` section: every action only the human can do (approve a production run, supply a file, set a secret, decide). Whoever creates such a need adds the item at once, with a link or path and the reason; whoever sees it done removes it. Never leave an item stale. Repeat the current list at the end of every reply to the owner.
* **Proactive status:** post a one-line `STATUS` entry whenever you start, finish, block or change direction on a ticket, without being asked. Say what you need from the owner or another agent and from whom. Do not wait to be polled; a silent agent is assumed blocked.
* **Board layout:** the board opens with OWNER GOALS, OWNER TO-DO, a PULL REQUESTS table (one row per open PR: owner, state, next step; the coordinator keeps it current, authors update their row), then one STATUS entry per agent per ticket. Nothing else: resolved entries, handovers and acknowledgements are deleted once their outcome is in Jira or a PR.
* **Keep the board clean:** one entry per ticket per agent, edited in place rather than appended to. Delete your entries when the work is merged or the question is answered. Move decisions to the Jira ticket first (a comment), then prune. The board holds only what is open now.
* **Decision ids** carry the author: `D-claude-12`, `D-codex-3`, so two agents never reuse a number.
* **Every PR is reviewed by another agent before it merges.** The author never reviews its own PR. When you open a PR, post `REVIEW REQUEST #<n>` on the board; another agent (never the owner by default) reads the whole diff, not the summary, and posts the review as a PR comment: what is right, what must change (numbered, with file and reason), what is optional. The author fixes or answers each point on the PR, then the reviewer replies `APPROVED` there. Merge only after that, plus the proof and green checks. Look first for: unsafe defaults (fail-open instead of fail-closed), secrets in output, missing tests for the new rule, scope creep, and anything that contradicts the Jira ticket. If no other agent is active, the coordinator reviews; if the coordinator is the author, the next agent reviews. Record the outcome as a Jira comment on the ticket.
* **After a restart or a long gap**, read the board and Jira before acting, then post a status line.
* **Production writes** need `WRITE REQUEST`, a grant from the coordinator, the owner's approval, then `WRITE DONE` with the load id and counts. Release the slot in the same entry.

## 5. Commits & Pushes
* That action is always under my ID
* You need to identify yourself as a colaborator on commits or pushes

## Reference Examples
For concrete formatting of notes, targeted routing, and pruning workflows, see [examples.md](./examples.md).
- **Review cycle:** the reviewer lists all comments in one pass. After fixes, a re-review covers only commits added since the last review; no new comments on code already reviewed unless the new commits broke it. No comments means the reviewer approves and the coordinator merges. Authors never merge their own PR.

- **Next-actions block:** the coordinator keeps a `## NEXT FOR EACH AGENT` block near the top of the board, one bullet per agent with exact commands and paths, so the owner never has to relay instructions. Every agent reads it at the start and after every finished step.

- **Subject ids:** the board has a `## SUBJECTS` table (id = Jira key, `BOARD` for process). Every post heading and every element of a reply starts with the subject id, e.g. `### [AR-1355 | Codex | status | time]`. A new subject gets a table row first. This keeps posts deterministic and short.
