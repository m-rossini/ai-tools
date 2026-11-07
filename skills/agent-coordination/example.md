# Complete Agent Coordination Example

This file demonstrates a full end-to-end scenario of multiple CLI agents (Claude and Codex) coordinating across parallel worktrees using an ephemeral `COLLABORATION.md` scratchpad, resolving a question, and moving permanent decisions to Jira.

---

## Complete Lifecycle Scenario

### Step 1: Claude Posts an Interface Update & Question
Claude is working in a separate worktree on `feature-auth` and modifies a shared file. It leaves a note in `COLLABORATION.md`:

```markdown
### [Claude | worktree: feature-auth | Issue #102] - 2026-11-07 14:30
- **To:** @Codex
- **Note:** Switched the JWT payload structure in `src/auth.ts` to include user roles. If you need claims in your dashboard worktree, call `getUserClaims()`. Also, are you touching `db/migrations/`?
```

### [Codex | worktree: feature-dashboard | Issue #105] - 2026-11-07 14:32
- **To:** @Claude
- **Note:** Thanks for the heads-up on `getUserClaims()`. And no, I am not touching `db/migrations/`—go ahead!