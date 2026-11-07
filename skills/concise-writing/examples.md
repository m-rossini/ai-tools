# Concise Writing — Examples

## Example 1: Eliminating Non-Value-Adding Words

**Original (wordy):**
> We are currently in the process of evaluating the different options that are actually available to us for this project. It is basically necessary that we make a final decision by the end of the day on Friday.

**Filtered (removing non-value words):**
- `currently in the process of` → `are`
- `different` → redundant before `options`
- `actually available to us` → adds nothing beyond `options`
- `basically` → meaningless qualifier
- `make a final decision` → `decide`
- `the end of the day on` → `by`

**Revised (direct):**
> We are evaluating options for this project. We must decide by Friday.

**Comparison:**

| Metric         | Original  | Revised  | Reduction |
|----------------|-----------|----------|-----------|
| Word count     | 33 words  | 10 words | -70%      |
| Token count    | ~40 tokens| ~12 tokens | -70%   |
| Cognitive load | High (buried deadline) | Low (clear action & deadline) | Immediate |

---

## Example 2: Reporting Status & Recommendations

**Avoid (fluffy):**
> Hi team! I wanted to reach out and give you a quick update regarding our database migration project. As you might know, we've been running into some unexpected latency issues over the past week. I spent some time analyzing the logs and I feel like it might be due to our index setup, but I'm not totally sure. I think we should probably pause the rollout for now just to be safe while we investigate further. Let me know what you think!

**Use (concise & data-backed):**
> Database query latency increased by **42%** following yesterday's deployment.
>
> **Root Cause:** Unindexed foreign key scan on `users.account_id` (verified via query execution plan).
>
> **Action:** Pausing rollout until index patch is applied.
>
> *Assumption: Current traffic baseline remains stable during the delay.*

---

## Example 3: Explaining a Technical Choice

**Avoid (fluffy):**
> Hope you're having a great day! When thinking about which hosting option we should go with, there are a lot of good arguments for serverless. It's really popular these days and many developers love it because you don't have to manage servers. In my personal opinion, it will probably end up saving us a lot of money in the long run because we only pay for what we use.

**Use (concise & data-backed):**
> Recommended Option: **Serverless Hosting**
>
> - **Cost:** Projected monthly cost is **$45/mo** based on current traffic (100k requests/day) vs. **$180/mo** for dedicated instances.
> - **Maintenance:** Zero infrastructure management required.
