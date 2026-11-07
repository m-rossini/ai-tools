# Proposal Writing System

## The Formula

Every proposal follows this structure. No exceptions.

```
HOOK (1-2 sentences)
→ Show you understand their specific problem. Reference something from THEIR job post.

PROOF (2-3 sentences)
→ ONE relevant product. What it does. How it maps to their need. Include link.

APPROACH (2-3 bullets)
→ How you'd tackle THEIR project. Be specific to their stack/requirements.

CLOSE (1 sentence)
→ Concrete next step. Call, outline, or deliverable offer.
```

Total: Under 200 words. Always.

---

## Voice & Tone

Pedro's proposal voice is:
- **Confident but not arrogant.** "I've built this before" not "I'm the best at this."
- **Direct.** No filler, no hedging. Get to the point.
- **Technically specific.** Use their terminology. Reference their stack if mentioned.
- **Slightly informal.** Not corporate. Not chatty. The tone of a sharp engineer who respects the client's time.
- **Consultative.** Show you're thinking about their problem, not just selling your hours.

### Words Pedro Uses
- "ship," "build," "architect," "wire in," "enforce," "deploy"
- "production," "live," "real users," "Stripe payments"
- "deterministic," "structured output," "confidence scoring"
- "hallucination-proof," "server-side enforcement"

### Words Pedro NEVER Uses
- "leverage," "synergize," "utilize," "facilitate"
- "I am passionate about..." 
- "Dear Sir/Madam" or "Dear Hiring Manager"
- "I am writing to express my interest..."
- "I believe I would be a great fit..."
- "Please feel free to reach out..."
- "I look forward to hearing from you"
- Any emoji in proposals

---

## Example Proposals By Job Category

### Example 1: "Integrate Claude API Into Our App"

**Job post (hypothetical):** "We have a Next.js SaaS app and want to add Claude to generate summaries of user-uploaded documents. Need someone who's worked with the Anthropic API before."

**Proposal:**

You need Claude generating reliable document summaries without hallucinating facts from the source material — that's the real challenge, not the API call itself.

I built AreaIQ (area-iq.co.uk), a UK area intelligence platform where Claude Sonnet writes full narrative reports from government data. The key: scores are computed deterministically first, locked, then passed to Claude as context with server-side enforcement so the AI literally cannot modify the computed values. Same architecture principle applies to your summary use case — ground the model, validate the output.

For your project, I'd approach it like this:
→ Document parsing pipeline (PDF/text extraction → structured chunks)
→ Claude integration with structured output schemas and source-grounding
→ Validation layer to check summaries against source content before serving to users

Happy to walk through the architecture in a quick call this week. I can also share a brief technical outline beforehand if that's useful.

---

### Example 2: "Build Me an AI-Powered MVP"

**Job post (hypothetical):** "Looking for a developer to build an MVP for a startup idea. It's a tool that uses AI to analyze competitor pricing. Need auth, a dashboard, and basic payments."

**Proposal:**

Competitor pricing analysis with AI — I've built almost exactly this. OscarAI (oscar-ai.com) is a competitive intelligence tool for UK alcohol brands: scrapes 15+ retailers in real-time, runs Claude-powered analysis on pricing and positioning, and generates confidence-scored action recommendations with a full audit trail.

Your MVP needs the same core pieces and I've shipped all of them before:
→ Auth (I use NextAuth v5 with OAuth — 15 minutes to production)
→ Competitor scraping pipeline with caching (I've built this for 15+ data sources)
→ AI analysis layer with structured outputs and confidence scoring
→ Dashboard with filterable views + Stripe payments (4 tiers on AreaIQ)

I ship fast — AreaIQ went from zero to live with 57+ features in weeks. Happy to jump on a call to scope the first version and give you a timeline.

---

### Example 3: "Fix Our AI Prompts / Improve Output Quality"

**Job post (hypothetical):** "Our chatbot gives inconsistent answers and sometimes makes things up. We use GPT-4. Need someone to audit and fix our prompt system."

**Proposal:**

Inconsistent outputs and hallucination usually come from the same root: the model has too much freedom and not enough structure. I've solved this in production across multiple live products.

In AreaIQ, Claude writes detailed area reports but can't override computed scores — they're locked server-side before the model sees them, then re-enforced over the output. In OscarAI, every AI-generated recommendation includes a confidence score and gets tracked against actual outcomes so you can measure when the model drifts.

For your chatbot, I'd start with:
→ Audit your current prompts — identify where format, tone, and factual accuracy break
→ Restructure with output schemas, few-shot examples, and guardrails
→ Add a validation layer between GPT output and what reaches the user

I can do an initial audit and deliver a findings report within 3-4 days. Want to share access so I can take a look?

---

### Example 4: "Build a Scraping / Data Pipeline"

**Job post (hypothetical):** "Need to scrape product data from multiple e-commerce sites and organize it in a database with automated updates."

**Proposal:**

I built exactly this for OscarAI — a scraping engine that pulls product data from 15+ UK retailers with a 15-minute cache refresh cycle, normalises it, and feeds it into a Postgres database for AI-powered analysis.

The tricky parts are resilience (sites change their markup), deduplication, and keeping the cache fresh without hammering the sources. I've solved all of these.

For your project:
→ Puppeteer-based scraping with per-site parsing configs (easy to add new sources)
→ Automated scheduling with configurable refresh intervals
→ Normalised Postgres schema with dedup logic
→ Dashboard to monitor scrape health and data freshness

If AI analysis on the scraped data is something you'd want later, I can architect the pipeline to feed into Claude or GPT from day one. Happy to scope the first version this week.

---

### Example 5: "AI Chatbot / Assistant For My Business"

**Job post (hypothetical):** "Want to build a customer-facing AI chatbot for our SaaS product. Should answer questions about our docs and help users troubleshoot."

**Proposal:**

The gap between a chatbot demo and one that actually works in production is huge — mostly around keeping the model on-topic and not making things up when it doesn't know the answer.

I've built controlled AI output systems across 4 live products. In AreaIQ, Claude generates detailed reports but operates within strict guardrails: it receives pre-computed data as context and can't deviate from it. Same principle applies to a docs chatbot — ground the model in your actual content, enforce output structure, and handle the "I don't know" case gracefully.

For your chatbot:
→ Ingest and chunk your docs into a searchable format (RAG pipeline)
→ Claude or GPT retrieval layer that grounds answers in your actual content
→ Confidence scoring — if the model isn't sure, it says so instead of guessing
→ Admin view to see what users are asking and where the bot struggles

Want to share your docs/product so I can sketch the architecture?

---

## Proposal Customisation Checklist

Before sending any proposal, verify:

- [ ] First sentence references something SPECIFIC from their job post
- [ ] Only ONE product mentioned (the most relevant one)
- [ ] Product link included
- [ ] Approach bullets are specific to THEIR project, not generic
- [ ] Under 200 words
- [ ] No Webskitters mention
- [ ] No "Dear Hiring Manager" or corporate filler
- [ ] Close has a concrete next step
- [ ] Rate/price only included if it's a fixed-price job (for hourly, let them set the budget discussion)
- [ ] Read the job post twice — is there anything you missed?

---

## Handling Common Client Objections

### "Your rate is too high"
"I understand — happy to discuss scope. I can usually find ways to deliver the core value in a leaner first phase, then expand from there. What's most important to get right in v1?"

### "Can you do a test project first?"
"Absolutely — I'd suggest a small paid scoping exercise ($200-500) where I audit your current setup and deliver a technical plan. That way you see my work quality before committing to the full build."

### "We need this done ASAP"
"Fast delivery is what I do — AreaIQ went from zero to live with 57+ features in weeks. Let's jump on a call today and I can give you a realistic timeline based on scope."

### "Have you done [exact thing] before?"
If yes: point to the product. If not: map the closest product to their need and explain the architectural similarity. Never lie. "I haven't built [exact thing], but the architecture is very similar to [product] where I [specific parallel]. The core challenge is [X] and I've solved that."

---

## Rate Negotiation

### Never Negotiate Against Yourself
- Don't preemptively lower your rate. Quote your rate. If they push back, THEN discuss.
- Frame rate conversations around value: "My rate reflects that I've shipped this before — which means faster delivery, fewer revisions, and production-quality architecture from day one."

### The "Starter Rate" Play
For your first 3-5 AI jobs on the revamped profile, slightly below-target rates are fine. Frame it as: "I'm offering a competitive rate for this project because I'm building out my AI-specific portfolio on Upwork. My next project at this scope will be at [higher rate]."

This is honest, creates urgency, and clients appreciate the transparency.

### Fixed Price vs Hourly
- **Prefer fixed price** for well-scoped projects. You work fast — hourly undervalues you.
- **Prefer hourly** for open-ended projects, ongoing retainers, or when scope is unclear.
- **Never accept hourly with time tracking screenshots** for AI/prompt engineering work. It's not a sweatshop. If a client insists on Upwork's time tracker for creative/AI work, that's a red flag.
