# Pedro's Complete Product & Experience Portfolio

Use this reference when writing proposals or assessing job fit. Every entry includes what it proves and which client needs it maps to.

---

## AI-Native Products (Solo-Built, Live)

### AreaIQ — UK Area Intelligence SaaS
- **URL:** area-iq.co.uk | **GitHub:** public
- **Status:** Live with Stripe payments, 57+ features shipped
- **What it is:** Score any UK postcode across safety, schools, transport, amenities, environment using 5 live government APIs. Intent-driven scoring — a family moving house and a restaurant owner get different scores for the same area.
- **AI architecture:** Claude Sonnet writes the narrative report but NEVER sets scores. Scores are computed by a deterministic TypeScript engine (16 functions, 4 intent profiles, 3 area-type benchmarks), locked, passed to AI as context, then server-side enforced over the AI output. Hallucination literally cannot corrupt the computed result.
- **Production features:** Google OAuth, Stripe (4 tiers), REST API with Bearer auth, API key management, rate limiting, MRR dashboard, PDF export, email delivery, GDPR compliance, embeddable widget, programmatic SEO pages for 7 UK cities.
- **Stack:** Next.js 16, React 19, TypeScript, Neon Postgres, NextAuth v5, Stripe, Claude Sonnet 4, Vercel
- **Proves:** Production LLM integration, hallucination containment, API design, full SaaS delivery, payment systems, data pipeline architecture
- **Best for proposals about:** AI integration, SaaS development, API development, data analysis platforms, prompt engineering, hallucination prevention, UK property/location tech

### PhantomOS — Gaming Merchandise Intelligence
- **URL:** phantom-os.vercel.app | **GitHub:** public
- **Status:** Live multi-tenant SaaS
- **What it is:** AI-powered merchandise intelligence for gaming publishers. Aggregates sales data across platforms, maps products to IP assets using Claude, surfaces insights into which characters and themes drive revenue.
- **AI architecture:** Claude-powered tagging pipeline with confidence scoring. Products are automatically mapped to game characters/themes via LLM with human-reviewable confidence thresholds.
- **Key features:** IP Asset Graph (proprietary product-to-character mapping — doesn't exist elsewhere), multi-tenant RBAC, Shopify OAuth, AES-256-GCM credential encryption, Upstash rate limiting, full audit logging.
- **Decision discipline:** Explicit framework killed 4 major feature areas to preserve strategic focus on the IP Asset Graph moat.
- **Proves:** AI-powered data classification, confidence scoring, multi-tenant architecture, strategic product thinking, gaming/entertainment domain knowledge, Shopify integration
- **Best for proposals about:** AI tagging/classification, e-commerce intelligence, Shopify integration, gaming tech, multi-tenant SaaS, data mapping

### OscarAI — UK Alcohol Competitive Intelligence
- **URL:** oscar-ai.com | **GitHub:** public
- **Status:** Live
- **What it is:** Competitive intelligence for UK alcohol brands. Scrapes 15+ retailers in real-time, runs AI analysis on pricing/positioning/availability, generates confidence-scored action recommendations.
- **AI architecture:** Claude generates action recommendations with confidence scores. Full audit trail — every AI recommendation tracked against actual revenue impact with rollback available on any executed action.
- **Key features:** 15-minute cache refresh scraping engine, UK events calendar triggering seasonal demand analysis, action audit trail, competitor price tracking.
- **Proves:** Web scraping at scale, real-time data pipelines, AI-powered recommendations with accountability, competitive intelligence systems
- **Best for proposals about:** Scraping/data pipelines, competitive intelligence, real-time analytics, AI recommendations, retail/CPG tech, price monitoring

### DataDuel — Higher-or-Lower Trivia Game
- **Status:** Started, not finished. ⛔ NO LIVE LINK — NEVER link in proposals
- **What it is:** Interactive trivia game using real-world datasets. Players guess which of two items has a higher value across various categories. Father-son project.
- **Proves:** Rapid prototyping, data visualization, game mechanics, collaborative building
- **Best for proposals about:** Interactive apps, gamification, data-driven UIs, quick MVP builds
- **How to reference:** Only mention casually if relevant ("I've prototyped data-driven game mechanics"). Low priority — use other products first.

---

## Construction & Operations Tech (Solo-Built)

### SiteTally — QR Code Asset Tracking for Construction
- **URL:** site-tally.vercel.app
- **Status:** Live ✅ LINKABLE IN PROPOSALS
- **What it is:** Construction site asset tracking via QR codes. Scan any piece of equipment to see its status, location, maintenance history, and assignment.
- **Proves:** QR code systems, asset management, construction industry understanding, mobile-responsive web apps
- **Best for proposals about:** Construction tech, asset tracking, QR systems, field operations tools, inventory management

### SiteSense — AI-Powered CIS Compliance Invoice Processing
- **Status:** Started, not finished. ⛔ NO LIVE LINK — NEVER link in proposals
- **What it is:** Automated invoice processing for UK construction contractors. Uses AI to parse invoices and verify CIS (Construction Industry Scheme) compliance, flagging issues before submission.
- **Proves:** AI document processing, regulatory compliance automation, UK construction industry knowledge, invoice/financial data handling
- **Best for proposals about:** Document processing, AI for compliance, fintech/accounting automation, construction industry tools, UK tax/regulatory systems
- **How to reference:** Mention as domain experience ("I've worked on AI-powered invoice compliance processing for UK construction") but NEVER say "check it out" or include a link. Frame as architecture/domain knowledge, not a shipped product.

---

## Career & HR Tech (Solo-Built)

### Traiblix — AI Career Intelligence Platform
- **Status:** Started, not finished. ⛔ NO LIVE LINK — NEVER link in proposals
- **Stack:** Supabase, Next.js
- **What it is:** AI-powered career platform with resume analysis, job matching, career coaching, and progress tracking.
- **Features built:** Resume parsing and scoring, AI-generated career recommendations, job market matching, progress dashboards.
- **Proves:** AI for HR/recruitment, resume/document parsing, recommendation systems, career coaching workflows
- **Best for proposals about:** HR tech, AI resume screening, career platforms, recruitment tools, job matching algorithms
- **How to reference:** Mention as architecture experience ("I've built AI resume parsing and job matching systems") but NEVER say "check it out" or include a link. Frame as technical capability, not a shipped product.

---

## Client Work & Agency Experience

### IV Creative Ltd (Manchester) — Technical Product Specialist
- **Duration:** Jun 2024 – Feb 2025
- **Context:** Creative agency specializing in gaming merchandise and digital products. Clients included Coca-Cola, Black Mirror, Wobbly Life, Enshrouded.
- **What Pedro did:**
  - Built OscarAI end-to-end as an internal/client tool
  - Shipped client portal with RBAC, filterable dashboards, PDF export (adopted by 4 clients)
  - Rebuilt BlackMirror interface into a component-based design system
  - Established company web delivery capability from scratch
  - Closed a £45K enterprise deal
  - Opened commercial conversations with 10+ prospects via AI product demos
  - Created internal insights platform that halved pitch preparation time
  - Defined pricing models and service packages across digital offering
- **Proves:** Enterprise delivery, client management, design systems, agency workflows, gaming/entertainment industry, commercial acumen
- **Best for proposals about:** Client portals, dashboards, design systems, agency work, gaming industry projects, enterprise deals

### Webskitters Technology Solutions (London) — Product Pre-Sales Engineer
- **Duration:** Mar 2024 – Jun 2024
- **What Pedro did:**
  - Built the UK operation from scratch (hired 5-10 person team)
  - Led 40+ client engagements end-to-end
  - Grew UK accounts to £500K+ combined
  - Discovery, scoping, architecture, sprint planning, delivery handover
- **Proves:** Team leadership, client management at scale, pre-sales engineering, offshore/onshore coordination
- **Best for proposals about:** Technical consulting, project management, multi-stakeholder delivery
- **Note:** Keep this entry minimal in proposals. It's agency work and shouldn't anchor Pedro's current positioning.

---

## Commercial & Sales Background

### Revenue Track Record
- £500K+ in delivery accounts grown (Webskitters UK)
- £60K+ direct revenue generated (Bluetown SaaS sales)
- £45K single enterprise deal closed (IV Creative)
- 40+ deals closed end-to-end
- 15+ clients retained through account management
- 10+ enterprise prospects opened via AI product demos

### Sales Skills (Use Subtly in Proposals)
Pedro's sales background means he understands:
- **Discovery:** He'll ask the right questions before building. Clients love this.
- **Stakeholder management:** He knows how to communicate with non-technical decision makers.
- **Scoping:** He can translate vague requirements into structured specifications.
- **Commercial framing:** He thinks about ROI, not just features.

These should NEVER be stated directly in proposals. Instead, they should be demonstrated through how the proposal reads — consultative, specific, shows understanding of the client's business problem, not just the technical task.

---

## Technical Stack Reference

### Primary Stack (What Pedro Ships With)
- **Frontend:** Next.js (App Router), React, TypeScript, Tailwind CSS
- **Backend:** Next.js API routes, REST API design, Drizzle ORM
- **Database:** Neon Postgres, Supabase
- **AI:** Claude API (Anthropic), GPT-4 (OpenAI), Gemini
- **Auth:** NextAuth v5, Google OAuth, GitHub OAuth
- **Payments:** Stripe (Checkout, Customer Portal, webhooks)
- **Deployment:** Vercel
- **Scraping:** Puppeteer, custom scraping engines
- **Dev tools:** Claude Code, Cursor, Jira, GitHub, Figma

### Secondary Stack (Competent But Not Lead)
- AWS (EC2, S3, CloudFormation, CloudFront, CloudWatch)
- Python
- Shopify (Headless, Liquid, Hydrogen)
- WordPress (legacy, don't lead with this)

### Design Philosophy
- Dark, data-dense, Bloomberg Terminal aesthetic
- No rounded corners, no gradients, no shadows
- Monospace for data values
- Geist Sans/Mono typography
- Component-based design systems
- Clients consistently respond to this aesthetic — it signals "serious engineering" not "template"

---

## Certifications & Education

- **AWS Cloud Practitioner** — Cloud infrastructure competency
- **IBM AI Fundamentals** — AI/ML foundations (Credly verified)
- **Google Analytics Certified** — Product analytics
- **Marketing and Data Analytics** — University of East London
- **IBM Project Management Fundamentals** — PM foundations

---

## Languages

- **English:** Native-level fluent
- **Portuguese:** Native fluent — advantage for Brazilian/Portuguese clients
- **Spanish:** Fluent — advantage for Latin American/Spanish clients

This is a genuine competitive advantage on Upwork. Many AI jobs are posted by non-English-speaking founders who prefer working in their language. Portuguese and Spanish fluency opens markets that monolingual freelancers can't access.
