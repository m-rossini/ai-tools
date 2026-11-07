---
name: onegoodarea
description: "This is the masterreference of onegoodarea"
---


OneGoodArea
Reference & Playbook
OneGoodArea
The Master Reference & Playbook
Everything about OneGoodArea, from nothing to more than almost anyone.
Written for two readers at once: the newcomer who has never heard of the company, and the expert who wants the exact shape of every product, endpoint, and concept. Read it top to bottom the first time; use it as a reference after.

Accuracy contract. Parts I–VIII and X describe what exists in the product today. Anything planned is labelled explicitly as roadmap. Part IX (Trajectory) is forward-looking by design. Nothing here is aspirational unless it says so; this document does not invent capabilities.

Contents
I
The company
What we are, the thesis, mission, principles
II
The foundations
Geography, signals, determinism, the corpus
III
The four products
Signals, Scores, Monitor, Intelligence
IV
The API surface
Auth and every endpoint
V
The data
Every source and the methodology
VI
The platform
Architecture, Levers, MCP, metering
VII
The business
ICPs, commercial model, competition, moat
VIII
Worked examples
End-to-end journeys
IX
Trajectory
Where we are going
X
Deep dives
Architecture, scale, data, training, gaps, pricing
XI
The exhaustive glossary
Every term, defined in depth
Part I
The company
01
Part I
What OneGoodArea is, starting from nothing
Imagine you want to make a serious decision about a place in the UK. Maybe you are a bank deciding whether to lend against a house. Maybe you are an insurer setting the price of a home policy. Maybe you are a council deciding where to put a service, or a property website trying to tell a user something true about a neighbourhood.

To make that decision well, you need real facts about the area: how much crime there is and whether it is rising or falling, how the schools are rated, how deprived the area is, what houses actually sell for and which way prices are moving, whether it floods, what is nearby, how well connected it is.

All of that data exists. It is public. But it is published in a dozen different places, on a dozen different schedules, at a dozen different levels of geography, in a dozen different formats. None of it comes with a guarantee that it will not change under you. None of it remembers what it looked like last month. And none of it is shaped so a computer program can just ask it a question.

OneGoodArea is the layer that fixes all of that. We gather the public area data once, clean it, line it up to a common geography, attach a source and a trust level to every number, store it, capture a fresh copy every month so it builds a history, and expose the whole thing as a programmable layer other software can build on. On top of that layer we offer a defensible scoring engine, a way to monitor a whole book of areas for change, and a way to ask the data questions in plain language that get turned into precise, auditable queries.

OneGoodArea is the data and intelligence layer underneath UK property workflows: deterministic signals, configurable scoring, portfolio monitoring, and a typed AI query plane over monthly area time-series.

02
Part I
What OneGoodArea does, the job plainly
We do four jobs, and they map exactly to our four products.

Signals
The raw facts about any UK area, cleanly. Every data point addressable on its own, with its source and a trust level.

Scores
Those facts turned into one defensible 0 to 100 number, by transparent rules a risk committee can pin and defend.

Monitor
Watch a book of areas and get alerted when a signal moves or crosses a line you set.

Intelligence
Ask the whole dataset questions: rank, compare, find peers, find outliers, forecast, in plain language or typed queries.

Everything else the company does exists to make those four jobs deeper, more defensible, and harder to leave.

03
Part I
The core thesis: why we are infrastructure, not a lookup tool
This is the most important section in the document, because it is the difference between a small company and a large one.

The trap: the postcode lookup tool
There is an obvious version of this business, and it is the wrong one: a website where a person types a postcode and gets back an opinion, “this area scores 72 out of 100, it is pretty good.” Call it the lookup tool. It has three fatal problems:

Problem 01
It sells an opinion to a human. The output is a page read once. Nothing to build on.

Problem 02
Its switching cost is zero. A nicer tool appears and the user leaves. No lock-in.

Problem 03
The valuable part is trapped inside a report. You cannot get a signal on its own or compare a thousand areas.

A lookup tool is a consumer product with consumer economics: low price, high churn, no defensibility.

The real business: the infrastructure layer
The valuable version flips every one of those problems:

We sell an addressable layer to software. The output is data another system builds on. The buyer returns on every transaction they process.
The switching cost is high. Once a customer wires their underwriting model, portfolio book, and custom index into our layer, leaving means re-plumbing their whole workflow.
Nothing is trapped. Every signal is individually addressable, queryable across all areas, feedable into their own model. The score is one optional thing you can ask for.
This is the shape every winning B2B data company shares. The clearest example is HazardHub, which built exactly this shape for US property peril data (an addressable layer of risk variables, with optional per-peril scores an underwriter feeds into their own model) and was acquired by Guidewire, the core software system insurers run on. We are building that shape for UK area data.

The one-line test
Does this make us more of a data infrastructure layer, and less of a postcode-report website? Depth on the corpus beats breadth and flash, because the corpus is the moat and the corpus compounds.

04
Part I
Mission, vision, and where we are going
Mission
Make the true state of every UK area legible (cleaned and lined up), defensible (source, confidence, pinnable version), and programmable (reachable by software), so any organisation can build a better decision on top of it.

Vision
Become the default data and intelligence infrastructure for UK area decisions, the way a developer reaches for a payments or mapping API without a second thought. Then repeat it in every market with public area data and regulated area decisions.

The arc, in one breath. We start as the cleanest addressable layer of UK area signals. We become the layer with the longest memory, because monthly capture builds a time-series nobody else has. We add the intelligence plane that turns memory into screening, monitoring, and forecasting. We add Levers, so every enterprise pins its own version and builds its own index on our data, making us part of their regulated stack. And at the frontier we stop only aggregating public feeds and start generating our own proprietary signals, including from earth observation, so the truth about how UK places change is something only we hold. The full arc is Part IX.

05
Part I
The principles that make us us
Not decoration. Each is a load-bearing commitment that shapes the product and the sale.

01
AI never sets the numbers
Every number comes from the database. AI is an interface and a planner, never the source of a value. This one rule is what makes the product saleable to banks and insurers.

02
Deterministic by default
The same input produces the same output, every time, until a version is deliberately changed. No drift, no surprises.

03
Provenance on everything
Every value carries where it came from, when it was released, and how much to trust it.

04
No invented claims
We advertise only what is live in code and reachable on an endpoint. The credibility this buys is what lets us sell into regulated buyers.

05
The corpus is sacred
Every month we fail to capture is data we can never recover. The monthly snapshot is the most important recurring job in the company.

06
Depth beats breadth
Given one more shallow feature or one more layer of depth on the data we already have, depth wins.

07
Honest degradation
When data is missing or weak, we say so through the confidence system. We never dress a proxy up as a primary source.

Part II
The foundations
The concepts you must understand before the products make sense. Each explained from scratch, then to depth.

06
Part II
UK area geography, the ground everything sits on
Everything OneGoodArea does is attached to a place, and to be precise about places you need the official geography. Here is the whole ladder.

Unit	What it is
Postcode	The thing everyone knows (e.g. M1 1AE), a dozen or few dozen addresses. The user input; too small and personal to store at, so we translate it up.
LSOA	Lower-layer Super Output Area, the workhorse unit in England & Wales, ~1,500 residents, ~35,000 of them. Codes like E01005207. Most of our data is stored at this grain.
Data Zone	The Scottish equivalent, ~500–1,000 residents, codes starting S01.
MSOA	Middle-layer Super Output Area, several LSOAs, used for some coarser data.
LAD	Local Authority District, the council level (e.g. Manchester). Used to scope queries.
Boundary vintages matter. Statistical geographies are periodically redrawn. The current English deprivation index uses 2021 boundary codes; some datasets still use 2011 codes. When two datasets use different vintages they do not line up, and reconciling them is real work (a live coverage gap for Wales and Scotland, on the roadmap).

Why area level, not property level. Most public data only exists at area level; and working at area level means we hold no personal data about individuals. The smallest thing we describe is an area of ~1,500 people, never a person, household, or specific property. That is a deliberate privacy stance, central to how we talk to buyers and regulators. Property-level granularity is roadmap, and would preserve the same posture.

07
Part II
What a signal actually is
A signal is the atom of the whole system: a single, named, addressable fact about an area, with metadata attached. Learn its anatomy and much of the product falls into place.

Key	A stable machine name, e.g. crime.total_12m or property.median_price. How software addresses the signal.
Category	The family: crime, property, deprivation, and so on.
Value	The actual number or band, e.g. 1,200 crimes, or £250,000.
Unit & direction	What it means and whether higher is better. Crime is lower_is_better; a good school rating is higher_is_better.
Confidence	A 0 to 1 trust level with a plain-language reason (section 9).
Observed period	The time the value describes, e.g. Apr 2025 to Mar 2026. What makes history meaningful.
Source	Which official body it came from, e.g. Police.uk.
The critical idea: a signal is addressable on its own. In a lookup tool the crime number is trapped inside a report. Here, crime.total_12m for an area is a thing you can fetch by itself, compare across areas, filter on, rank by, and feed into your own model. That is the whole difference between a report and a data layer.

Two kinds exist: raw signals, ingested directly (crime counts, sold prices, deprivation deciles, Ofsted ratings, flood risk); and derived signals, computed by us from the raw ones and the history (year-on-year change, trend slope, momentum, peer-relative z-score). Derived signals (section 12) are a big part of the moat, because they are what make the data screenable and predictive.

08
Part II
Determinism, and why regulated buyers need it
Deterministic means the same input always produces the same output, exactly, every time, until we deliberately change a version.

This is not a technicality but a commercial cornerstone. A bank or insurer using a number in a regulated decision has to answer their regulator's question: “why did this number come out this way, and will it be the same tomorrow?” A typical AI tool cannot promise this, because ask it the same thing twice and you can get two answers. Our engine can: scoring is computed by fixed, transparent rules, and after any AI step runs, the computed numbers are re-applied on the server so AI can describe them but never change them.

We reinforce this with version stamping (section 10): every result is stamped with the exact engine version that produced it, and a customer can pin to a version and know their numbers will not move until they approve a new one.

09
Part II
Confidence, honest trust on every number
Every signal and every score dimension reports a confidence: a number 0 to 1 that says how much to trust it, with a plain-language reason.

~1.0
High
Primary, fresh, well-covered (e.g. crime, every E&W LSOA).

~0.7
Medium
Partial data, an older dataset, or a limited sample.

~0.4
Low
A proxy stood in for the real thing.

~0.2
None
The data is missing for this area.

Two mechanisms make confidence honest rather than cosmetic:

Proxy clamping. If a value is a proxy, its confidence is clamped so it can never present as high, capped at medium no matter what. We never dress a stand-in up as a primary source.
Two-factor confidence for count-based signals. For sampled signals (crime, property medians), confidence reflects both how much data there is and how noisy it is. A median from three sales is less trustworthy than one from three hundred, and the confidence says so. This logic lives in shared modules that both the profile and scoring endpoints import, so a signal reports the same confidence everywhere.
Why it matters commercially: an underwriter cannot buy a black-box score. Confidence is the feature that turns “here is a number” into “here is a number you can defend.”

10
Part II
Provenance and versioning, defensibility made concrete
Provenance snapshots. Every time we ingest a source we write a snapshot record capturing the source, the release date, when we ingested it, the licence, a checksum (to prove the exact bytes), the row count, and free-text notes. For any number we serve we can show exactly where it came from and when, the paper trail a procurement or risk team asks for.

Engine versioning. The scoring methodology has a version (currently v2.0.2). It is stamped on every response and returned in the X-Engine-Version header. Through Levers (section 22) an organisation can pin to a version, so their numbers will not change until they explicitly approve a new one. That is the “no drift without approval” guarantee a regulated buyer needs.

11
Part II
The corpus and the time-series, the moat explained properly
The concept that makes us a large company

Most area data is a snapshot: the government publishes current figures, and when they publish the next version the old one is usually overwritten or forgotten. There is no widely-held, clean, small-area history. OneGoodArea does two things about this:

We persist, not fetch. Rather than fetching live every time (the naive way), we store it: a table of current values (signal_values) and a table of historical values (signal_timeseries), where every row is tagged with the observed period it belongs to.
We capture every month. A scheduled job appends the new period into the time-series. This is the moat clock. It has been running since May 2026.
Why it is a moat, not just hygiene: the history cannot be back-filled. A competitor starting next year can get today's data but never an accurate monthly record of what every UK area looked like over previous years, because that data was a snapshot that is now gone. Every month our clock runs, our lead grows, and it is a lead nobody can buy or rebuild.

The corpus also unlocks everything intelligent. You cannot detect change, find anomalies, or forecast without a history. Monitor needs it to know what changed; Forecast needs it to project a trend; the anomaly model needs it to know what is unusual. So the corpus is both the moat and the fuel for the whole Intelligence product.

12
Part II
Normalization, percentiles, derived signals, peer graphs
Four concepts that turn a pile of raw numbers into something you can screen, rank, and reason about.

Normalization
Raw signals are on wildly different scales (crime in the hundreds, prices in the hundred-thousands). To compare or combine them you put them on a common 0 to 1 scale, stored alongside the raw value. It is a prerequisite for scoring, peer distance, and anomaly detection.

Percentiles
Where each area sits relative to all others. “Crime in the 38th percentile” is instantly meaningful in a way “1,200 crimes” is not. Queries can filter and rank on percentiles as well as raw values.

Derived signals
Computed from raw signals and history: year-on-year change, trend slope (a regression line through the trailing window), short-horizon momentum (latest 6-month window versus the prior), and peer-relative z-score (how far an area is from its peers' average, in standard deviations, the anomaly signal).

Peer graph
For every area we pre-compute its peers: the most similar areas by normalized signal (nearest neighbours in signal space, not geography). Stored as a large materialised table (hundreds of thousands of rows). It powers “areas like this one,” comparables, and peer-relative anomaly signals.

The payoff: because derived signals compose exactly like raw ones, a single query can say “find English areas under £300k where prices are rising, crime is falling, and price is more than two standard deviations below peers,” and get a precise list back. That is a screen a lookup tool cannot answer at all.

Part III
The four products in depth
Products are the doors a customer walks through; capabilities (the store, models, Levers, metering) are the engine room every product draws on.

13
Product 01
Signals, “give me the data”
What it is. The addressable, source-backed, confidence-banded raw data layer for any UK area, plus the full area profile. Signals is the wedge and the land product: the simplest thing to buy, the thing a developer evaluates first, the foundation the other three stand on.

What you get. For a postcode or area, the full profile: every available signal across every category (crime and its 12-month trend, deprivation, property prices and YoY, flood, schools, amenities, transport), each with value, unit, direction, source, confidence, confidence reason, and observed period. Or one category at a time.

GET
/v1/area?postcode=M1 1AE
the whole profile
GET
/v1/signals/{category}
one category, filtered
Who buys it and why. Proptech platforms that want to build on clean UK area data rather than plumb thirteen feeds; any data or risk team that wants the ingredients for their own model, not our opinion. It is the entry point: land here, expand into Monitor and Intelligence later. A lookup gives one blended verdict; Signals gives you every ingredient separately, each defensible, each queryable.

14
Product 02
Scores, “give me a defensible number”
What it is. The deterministic scoring engine exposed as a product. When a customer genuinely wants a single 0 to 100 number (many workflows do), Scores provides one that is transparent, configurable, and defensible.

How the score is built. Real signals go into fixed, deterministic scoring functions producing a composite 0 to 100, broken into weighted dimensions (Safety and Crime, Schools and Education, Cost, Environment). Each dimension returns its own sub-score, plain-language reasoning line, and confidence. The composite is enforced server-side after any AI narration, so AI can describe it but never move it. The whole thing is stamped with the engine version.

Presets and custom weights. Four presets are just different weightings of the same signals for different purposes:

moving
business
investing
research
A customer can use a preset, supply custom weights, or (through Levers) save and pin their own org-specific presets. The moving preset is the lender / origination shape and weights Schools and Education at 20 percent.

POST /v1/score — area + preset or custom weights or preset_id → composite, dimensions with reasoning and confidence, weights used, engine version
Who buys it and why. Anyone who needs one defensible number in a workflow: a lender feeding an area score into an affordability model; a platform showing a transparent area rating. The value is not the number, it is that the number is pinnable, explained, and confidence-banded.

15
Product 03
Monitor, “watch my book”
What it is. Bulk enrichment plus change detection plus alerts over a portfolio of areas. Monitor is the retention and lock-in product: it wires a customer's live book of properties or areas to the moat and tells them when something moves.

How it works. A customer registers a portfolio. Every period, Monitor diffs this period's snapshot against the last. When a signal moves, or crosses a threshold the customer set, Monitor fires a signal.changed webhook to a URL they registered. Change detection depends on the time-series existing, you cannot detect change without a history.

A subtlety that shows the rigour. Some signals are static (deprivation updates only every few years, and when it does it is a methodology revision, not a real-world move). A naive change detector would fire a false alarm on a deprivation revision. So static signals must be excluded from change detection, or the first Monitor customer gets false alerts.

Endpoints. The /v1/portfolios family and the webhook subscription endpoints. Who buys it: insurers and lenders with a live book of exposures who need to know when an area's risk profile shifts; CRE firms monitoring target markets. The lock-in is structural, their book lives in our system.

16
Product 04
Intelligence, “ask questions of the moat”
The most advanced product, and the one most easily misunderstood. It is emphatically not a chatbot and not narrative. It is a smart query and insight plane over the corpus. The value is precise, typed, auditable questions answered from real data, not prose.

The query plane, POST /v1/query
The heart of Intelligence. There is a typed query-plan grammar: a JSON structure describing a question the corpus can answer. That JSON plan is the API. Natural language is just one way to produce a plan. Two input modes:

Programmatic · zero AI
The caller sends a {plan} (the JSON directly). The language model is never touched. The auditable, zero-cost path enterprises integrate against.

Natural language
The caller sends a {question}. Our planner (a Claude model) translates it into that same typed plan, which is validated and run. The answer comes from the database, identical in shape.

The plan grammar supports rank_areas, get_area, score_area, compare_areas, find_peers, find_insights, and find_forecast. Filters include eq, lt/lte/gt/gte, between, and percentile variants.

The non-negotiable principle: the plan is the contract, the database produces the answer, an invalid plan is rejected with a typed error and never silently reinterpreted. Every result traces to real store rows. This is what keeps Intelligence audit-safe and saleable to regulated buyers.

Insights & anomaly
POST /v1/insights
Rank areas by peer-relative z-score. “Which areas are moving more than two standard deviations from their peers?” Zero LLM in the hot path. Also Monitor's brain.

Peer groups
POST /v1/peers
k-nearest-neighbour over normalized signals: “areas like this one,” by signal fingerprint, not geography. The foundation for comparables and calibration.

Forecast
POST /v1/forecast
Project a signal forward. Linear regression over the trailing window gives a slope; the value is projected with an explicit confidence band, reported wide when the series is noisy.

The MCP surface
agent-era distribution
The whole query surface over the Model Context Protocol, so Claude Desktop, Cursor, Claude Code, and agents can reach our moat from inside a developer's own workflow (section 23).

The AI eval harness
A golden corpus of question-to-plan-to-answer cases measures the planner's accuracy. Baseline: 92.9 percent on the published corpus. An enterprise will not trust a natural-language layer on faith, but they will trust a measured number they can put in front of a risk committee.

Part IV
The API surface
17
Part IV
Auth, keys, rate limits, and quotas
Authentication
Every programmatic call carries a bearer token: an API key prefixed oga_, created in the dashboard.
IP allowlist
A key can optionally be locked to IP ranges (Enterprise control, part of Levers). A request from outside is rejected before anything else runs.
Rate limit
A per-minute cap per key (~30 requests/min) protects the service from spikes.
Monthly quota
Each plan has a monthly allowance, enforced in the request path. Hard tiers (free Developer) are cut off past allowance; higher tiers bill overage. The expensive natural-language path has its own tighter monthly sub-cap. On the free tier: 200 total calls/month, of which 10 may be natural-language.
Metering
Every call emits a usage event, both the billing substrate and a source of demand-signal insight.
18
Part IV
Every endpoint
Endpoint	Product	Purpose & returns
GET /v1/area	Signals	Full area profile: every signal with value, source, confidence, observed period
GET /v1/signals/{cat}	Signals	One signal category, filtered
POST /v1/score	Scores	0–100 composite, dimensions with reasoning & confidence, weights, engine version
POST /v1/query	Intelligence	Typed or NL query; returns ranked areas / peers / insights / forecast + the plan that ran
POST /v1/peers	Intelligence	Areas like this one, by normalized-signal distance
POST /v1/insights	Intelligence	Anomaly screen: areas ranked by peer-relative z-score
POST /v1/forecast	Intelligence	Project a signal; returns projected points with a confidence band
/v1/portfolios/*	Monitor	Manage a book of areas; portfolios, areas, and what changed
webhook subs	Monitor	Register a URL; receive signal.changed deliveries
GET /v1/me	Platform	Caller identity & entitlements: plan, api/mcp access, usage, limits, engine version, org
GET /v1/meta, /health	Platform	Service metadata (supported intents) and liveness
Part V
The data
19
Part V
Every source, in detail
All sources are public and UK-scoped. For each: what it gives, its geography, how it is treated.

Source	What it gives, and the nuance
Postcodes.io + ONS spine	Postcode to LSOA to MSOA to LAD, plus lat/lng and rural/urban class. The rural/urban class matters because thresholds differ.
Police.uk (crime)	Recorded crime, rolling 12-month total and monthly series, E&W, LSOA grain. Every LSOA covered, so high confidence. The monthly series feeds trend and momentum; change detection bites automatically.
Ofsted (schools, England)	School inspection outcomes. Nuance: Ofsted removed overall-effectiveness grades in Sept 2024, so a large, growing share have no overall grade, degrading a naive schools signal (coverage-aware confidence is roadmap). Estyn and Education Scotland are planned.
Deprivation indices	English IMD 2025 (2021 codes), Welsh WIMD 2019, Scottish SIMD 2020 (Data Zones). A static signal, revised only every few years, so it must be excluded from change detection.
HM Land Registry (prices)	Real sold prices (Price Paid): medians and transaction counts by area, with YoY change. Real transactions, not estimates. Sparse areas get lower confidence.
Environment Agency (flood)	Flood risk, cached at area grain so it does not leak more precision than the source supports.
OpenStreetMap	Nearby-amenities and connectivity context.
20
Part V
Methodology, how the raw becomes the defensible
The pipeline, in order, every month:

1
Ingest each source, writing a provenance snapshot.
2
Store raw values at area grain in signal_values, and append the period to signal_timeseries.
3
Derive the computed signals (YoY, trend slope, momentum, and after the peer graph, the peer-relative z-scores).
4
Normalize every signal to 0 to 1 and compute percentiles.
5
Refresh the peer graph (nearest neighbours per area).
6
Append the time-series period, advancing the moat clock.
Every step is idempotent (safe to re-run). Confidence is attached throughout, and proxies are clamped. Scoring reads all of this deterministically and stamps the engine version.

Part VI
The platform
21
Part VI
Architecture and stack
Monorepo, three workspaces plus a package. apps/web (Next.js frontend and its thin BFF proxies), apps/api (Fastify, all business logic), packages/contracts (shared typed contracts), and a standalone mcp/ package.
Strict separation. The web tier is a thin proxy, never running business logic or touching the database directly; it calls apps/api over HTTP. This is what lets the API stand alone as real infrastructure.
Data plane. Neon Postgres holds the signal store, time-series, peer graph, provenance, orgs, keys, usage, and subscriptions.
Hosting. apps/web on Vercel, apps/api on Render, Neon for Postgres. The monthly capture runs as a scheduled GitHub Actions job.
The Intelligence runtime. The planner uses a Claude model to translate a question into a typed plan. The plan, not the model, is the contract; programmatic callers skip the model entirely. A proprietary planner is on the roadmap.
22
Part VI
Levers, the configuration and lock-in layer
Levers is a cross-cutting capability, above all four products, not a product itself. It is how the platform is made bespoke per customer, and it is the switching-cost moat.

Orgs & members
Multi-tenancy: an org, its members, their roles.

Org-scoped API keys
Keys belong to an org, not just a user.

Custom Scores presets
An org clones, tunes, and pins its own scoring weights.

Custom Signals bundles
An org defines which subset of signals its keys can see.

Per-client Monitor thresholds
Custom alert rules per org.

Methodology pinning
An org pins the engine version its numbers use.

Per-org peer graphs, RBAC
Own peer set; owner / admin / member roles enforced.

White-label, IP allowlist
Org branding; keys locked to IP ranges.

Why it is the moat: once a customer's book, custom index, pinned version, and branded surface all live inside OneGoodArea, leaving means rebuilding their whole methodology somewhere else. Levers is how Enterprise is sold and how customers become permanent.

23
Part VI
MCP, the agent-era distribution channel
MCP (Model Context Protocol) is the standard by which AI tools call external tools. Our MCP server is a small standalone npm package (@oga-mcp/server) a developer runs on their own machine. It reads the developer's own API key from its config, checks entitlement against /v1/me, and exposes our query surface as tools the developer's AI (Claude Desktop, Cursor, Claude Code, any MCP client) can call inline: score a postcode, compare postcodes, get area signals, find areas, find peers, watch a portfolio, get portfolio changes, an area brief, plus static lookups like methodology and engine version.

The developer brings their own key. The server runs on their machine at their compute cost, but every tool call reaches our API, so the cost of serving the answer (and any language-model cost on the NL path) is ours. The key is how we identify and meter that usage.
Included on the free Developer tier and every paid package. A developer can put our layer inside their AI workflow at zero cost, the top of the growth loop, which is why a broken entitlement check on the free tier would be a lit-on-fire lead.
24
Part VI
Metering, billing and the demand-signal moat
Every API call emits a usage event, which does two jobs. First, it is the billing substrate: quotas and overage are computed from it. Second, it is a demand-signal moat: over time we learn exactly what the market asks for, which sharpens the product and the data investment in a way a competitor without our traffic cannot match.

Part VII
The business
25
Part VII
The ICPs and how each uses the products
Lenders & originators	Pin an engine version, feed the score and raw signals into an affordability or valuation model, defend the inputs to model risk. Land on Scores + Signals, expand into Monitor for the live book.
Insurers	Feed raw signals (flood, crime, deprivation) into their own pricing. Confidence and provenance are the unlock; they cannot buy a black box. Monitor watches their book for drift.
CRE & investment	Screen and compare markets at scale with Intelligence, monitor target areas, forecast a signal.
Public sector	Area-level intelligence for planning and service allocation, with a clean provenance story.
Proptech platforms	Embed the Signals layer as a feature instead of building the plumbing.
The motion is land and expand: land on Signals or a Core API contract, expand into Monitor and Intelligence, upsell Enterprise with Levers.

26
Part VII
The commercial model and pricing
Demo-led enterprise sales, with a free developer tier as the growth loop.

Package	Price	Includes
Developer	Free	A real key, 200 calls (10 NL), MCP included. Evaluation and top of funnel.
Core API	from £2,000/mo	Signals and Scores at production volume.
Decision Intelligence	from £5,000/mo	Signals, Scores, Monitor, and Intelligence together. The main package.
Enterprise Monitor	Custom	Levers, white-label, bespoke bundles and thresholds, methodology pinning, volume.
Annual contracts and paid pilots. The unit economics are strong: deterministic calls are served from a persisted, cached store at near-zero marginal cost, so the only real variable cost is the natural-language path, which is capped per tier. This is a high-margin infrastructure business, not a thin reseller.

27
Part VII
Competition and the moat, summarised
Consumer lookup tools
Crystal Roof, StreetCheck
Wrong shape, no lock-in. Not a real competitor for the infrastructure buyer.
B2B data vendors
Sprift, PropertyData
The closest comparables; they sell data points. Our edge: the compounding time-series corpus, confidence and provenance on every value, version-pinning, and the typed intelligence plane.
The reference shape
HazardHub → Guidewire
Proof that an addressable data layer with optional scores, fed into the buyer's model, is a valuable, acquirable business. We are building it for UK area data.
The moat in one paragraph. The corpus compounds monthly and cannot be back-filled. The models learn on the corpus, so they get better as it grows. And Levers locks in each customer's book, index, and version. Depth on the data beats breadth, and every month makes the lead larger.

Part VIII
Worked examples
28
Part VIII
A developer's journey
A developer at a proptech company wants area data in their product. They sign up for the free Developer tier, create an oga_ key, and drop the MCP server into their AI tool. They ask their assistant, inside their editor, “find English areas under £300k where prices are rising and crime is falling.” The MCP tool calls /v1/query, the planner turns the question into a typed plan, the database returns five areas with the real numbers, and the developer sees the layer work against live data before ever speaking to sales. When they are ready for production volume, that is a Core API conversation.

29
Part VIII
A lender's journey
A lender wants a defensible area input for their affordability model. They pin engine version v2.0.2 through Levers, so their numbers will not move without their approval. They call POST /v1/score with the moving preset for each application's postcode, read the dimension-level reasoning and confidence, and feed the score into their model, with the provenance snapshot and the pinned version as the audit trail for model risk. They add Monitor over their live book so they are told when an area's risk profile shifts. That is a Decision Intelligence contract.

30
Part VIII
An insurer's journey
An insurer does not want our score; they want the ingredients. They pull raw flood, crime, and deprivation signals through Signals, each with its confidence and source, and feed them into their own peril pricing. They use Monitor to watch their book of insured addresses' areas for adverse change, and Insights to find the areas moving unlike their peers. Confidence and provenance are what let them put our data into a regulated pricing model. That is Decision Intelligence moving toward Enterprise Monitor as the book grows.

Part IX
Trajectory, where we are going
Forward-looking by design: the arc from what we are to what we intend to become. The fuller, more speculative version lives in the companion Vision & Roadmap document.

31
Part IX
Near term
Own the geography completely: address-level granularity for lenders and insurers, and full Scotland and Wales coverage. Make the series move with more dynamic sources. Land the first reference accounts. Replace the third-party planner with a proprietary model so Intelligence runs at near-zero cost with no external dependency. Harden for enterprise (security posture, SLAs, reference logos).

Mid term
A signal marketplace (third parties contribute signals). Embedded distribution (OneGoodArea inside other people's products). Outcome calibration (prove and sell that our signals predict real outcomes). The decision graph (how every area relates to every other). Real-time and event-driven for the fast sources.

Long term
Predictive area intelligence a regulated buyer can underwrite. The agent-native ground-truth layer for UK places. Every enterprise running its own pinned, audited index on our data, which makes us part of their regulated stack. Expansion into adjacent area decisions (retail, public services, infrastructure, climate).

The frontier
Stop only aggregating the public feeds and start generating proprietary signals nobody else has, including from earth observation (construction and development activity, land-use change, night-lights as an economic proxy, post-event flooding). Own the sensing, own the models, and make the way the industry represents area truth our way. Then repeat the whole playbook in every market with public area data and regulated area decisions.

Through all of it the guardrails hold: AI never sets the numbers, provenance and confidence on everything, the corpus is sacred, depth beats flash, no invented claims. The core funds the frontier. The frontier makes the core uncatchable.

Part X
Deep dives
Below the surface: the architecture, how it scales, exactly what data we hold, how we gather it, how the models are (and would be) trained, what is still missing, and the precise mechanics of pricing.

X.1
Part X
The architecture in depth
The topology
apps/web	Next.js 16 on Vercel. Public site, docs, dashboard, and thin BFF proxy routes. Renders UI and forwards authenticated calls; holds no business logic.
apps/api	Fastify on Render. Every piece of business logic: auth, key validation, rate limiting, quota, scoring, store reads/writes, the intelligence planner and executor, Levers, metering. This is “the infrastructure.”
packages/contracts	Shared, typed (Zod) definitions of every request and response. Both tiers import from here, so they can never silently disagree about a shape.
mcp/	@oga-mcp/server, the standalone MCP server a developer runs on their own machine. The data plane underneath all of it is Neon Postgres.
The request lifecycle of a scored call
A single POST /v1/score from the wire to the response, showing every gate:

1
Bearer auth. The oga_ key is validated. Invalid or revoked is 401; outside an IP allowlist is 403.
2
Rate limit. The per-key per-minute budget is checked. Over budget is 429.
3
Plan API access. The caller's plan must permit API access, or 403.
4
Monthly quota. The allowance is checked; a hard-tier caller over it is 429 (enforced in the path, not just displayed).
5
The handler runs. Resolves org context (Levers), reads signals from the persisted store, runs the deterministic scoring functions, applies confidence, and if asked lets AI narrate, after which the computed numbers are re-applied so AI cannot change them.
6
Version stamp (honouring any org methodology pin), then meter (a usage event), then respond.
Every product endpoint follows the same auth-then-gate-then-handler-then-meter shape; the gates live in shared middleware so behaviour is identical across endpoints.

Strict separation, safe shipping, and the schema
The BFF pattern. No business logic and no direct database access in apps/web. Its /api/* routes are thin proxies to apps/api. All gating, validation, and data access happen once, in the API. This is why “we are infrastructure” is true at the code level.
Strangler-fig and dark flags. New capability is added additively behind flags; pure logic is split from I/O and unit-tested before it goes live. The deterministic engine is a frozen golden master, versioned when it must change, and load-bearing decisions are recorded as architecture decision records.
The store schema. signal_values, signal_timeseries (the corpus), signal_percentiles, source_snapshots, peer_assignments, plus platform tables (users, api_keys, orgs and org_members, subscriptions, usage and activity, portfolios, webhook subscriptions and deliveries).
X.2
Part X
Scalability
Scalability here is mostly a consequence of one early decision: persist, do not fetch.

Reads are cheap and bounded. A naive tool fetches thirteen external feeds per request, so it is slow, fragile, and rate-limited by others. We serve from our own indexed Postgres, so a read is an indexed lookup, scaling with the database, not someone else's rate limit.
Caching drives marginal cost toward zero. Results are cached (~24h) and at real traffic the cache-hit rate is high, so most requests never touch heavy computation.
apps/api is stateless. No request depends on server memory, so it scales horizontally; Neon scales the data plane independently.
Heavy jobs are offline and idempotent. Ingesting, deriving, normalizing, and refreshing the peer graph happen in the monthly batch, not the request path, so latency is unaffected and a re-run is safe.
The one variable cost is bounded by design. Only the NL Intelligence path invokes a language model; it is capped per tier, and the roadmap replaces the third-party model with our own, removing even that cost.
The batch-job scaling lesson. Building the peer graph is a large computation, and Neon's serverless connection has a request-time cap, so a single monolithic query cannot do it. The solution was a per-area computation through a bounded pool of concurrent workers, one area per round trip, completing the whole graph (~675,000 peer rows for ~33,700 areas) reliably. Transient timeouts on big writes are wrapped in a retry.

Where the ceiling is, honestly. The API runs on a modest Render tier and Neon has usage limits; neither is a customer-scale configuration yet. Graduating the API to a scale-to-zero container platform and sizing Neon up are known, cheap steps taken when traffic warrants. Nothing in the architecture blocks scale; the current hosting is a cost choice for the pre-revenue stage.

X.3
Part X
The datasets in detail
Counts are point-in-time and grow with the monthly clock.

Dataset	Geography	Cadence	Scale & coverage
Crime (Police.uk)	LSOA, E&W	Monthly	~1.2M monthly rows over ~36 months; every E&W LSOA (high confidence)
Prices (HMLR)	LSOA / outcode	Monthly, ~24mo held	Real sold prices; medians and transaction counts; sparse areas lower confidence
Deprivation	LSOA / Data Zone	Every few years	One vintage per nation; England 2021 codes, Wales/Scotland 2011 codes
Schools (Ofsted)	School point, England	Periodic	~22,000 schools; only ~9,800 carry an overall grade after Sept 2024
Flood (EA)	Area-cached	Periodic	Flood risk, cached at area grain
Amenities / transport	Point / area	Periodic	Nearby-amenity and connectivity context (OpenStreetMap)
Geography spine	Postcode→LSOA→LAD	Stable	~35,000 LSOAs in E&W; rural/urban class per area
Derived catalog & peer graph. On top of raw signals we compute ~nine derived signals: YoY change (prices, crime volume), trailing-window trend slopes (crime, transaction counts), 6-month momentum (prices, crime), and peer-relative z-scores (crime, prices), all queryable the moment they exist. The peer graph is a materialised table of ~675,000 rows for the English estate.

Coverage matrix, honest. England is deepest and highest-confidence. Wales and Scotland are partial: their deprivation indices use 2011 boundary codes that do not fully line up with the 2021 codes the geocoder produces, so some Welsh and Scottish reads miss even though the data exists (active roadmap). Crime is England and Wales; schools are England only today.

X.4
Part X
How we gather data, the ingestion pipeline
Data enters through a monthly, idempotent, write-only pipeline.

The clock. A scheduled GitHub Actions job runs monthly, holding the database connection as a secret, each step wrapped in a retry so a transient timeout does not fail the run.
The step chain. Migrate the schema, refresh each raw source (write-only), derive non-peer signals, normalize, refresh the peer graph, derive peer-relative signals, normalize again, then append the period to the time-series. Each step is idempotent.
Geocoding. A postcode or place name is resolved to its LSOA through the geography spine. A result with no valid UK LSOA is rejected rather than allowed to leak through as a bad match.
Provenance on every ingest (source, release date, ingest time, licence, checksum, row count, notes), so every value is traceable.
Safety guards. Ingests carry sanity guards; the schools loader guards against a collapse in loaded rows so a broken upstream file cannot silently wipe coverage. Guards are tuned against real upstream behaviour (Ofsted's grade removal meant a legitimate drop a naive floor would have flagged).
Most sources are in the automated monthly cron; some very large historical loads (the multi-year crime archive) run in dedicated runs. The pipeline is not a script that runs once, it is the mechanism that keeps the moat clock ticking, so its reliability is a first-class concern.

X.5
Part X
How we train, and would train, our models
There are two distinct kinds of “model,” and conflating them is a common mistake.

The trainable-models capability (statistical / ML on the corpus)
The “AI learning” people ask about is statistical and machine learning on our own data, not fine-tuned language models. It is a ladder we climb as the corpus deepens:

Normalization
Every signal on a common scale.
Built
Peer-grouping
k-NN over normalized signals, materialised as the peer graph.
Built
Calibration
Test whether signals predict real outcomes (default, claims, price moves, tenant demand), and re-weight by proven power.
Roadmap
Anomaly
Peer-relative z-scores flag areas moving unlike peers. Monitor's brain.
Built
Forecasting
Regression over the trailing window projects a signal forward with a band.
Built
The training data for all of this is the corpus itself, which is why the corpus is the asset. Nobody else has a small-area UK time-series of this shape to train on, and every month ours gets longer.

The planner model (natural language to typed plan)
The Intelligence NL path uses a language model as a planner: it translates plain English into our typed query plan. It never sets a number (an invalid plan is rejected with a typed error, never guessed at), and its accuracy is measured, not assumed: the eval harness scores it against a golden corpus with a structural match, baseline 92.9 percent.

Today the planner is a third-party Claude model. The roadmap is to train our own proprietary planner on the corpus of real questions and the plans they should produce. We accumulate exactly that training data through metering and planner logs (with per-key opt-out and retention limits), so every natural-language query makes the future proprietary planner better. When it lands, the NL path costs us nothing per call and depends on nobody else. That is the flywheel: usage generates the training data that removes the last variable cost and deepens the moat.

Data governance for training. Area-level data with no personal information; per-API-key opt-out of training capture; retention limits on captured planner and brief data; internal-only access to raw captured data, with aggregate-only visibility in tooling.

X.6
Part X
What is missing, the honest gaps
In rough priority

Address-level granularity	We are area-level; lenders and insurers eventually want property-level. The biggest data-expansion item, built to keep the no-personal-data posture.
Full Scotland & Wales	The 2011-vs-2021 boundary-code mismatch limits Welsh and Scottish deprivation reads. A boundary-normalization lookup fixes it (tracked and assigned).
Ofsted grade-removal	Grades removed Sept 2024 structurally weakened the schools signal; coverage-aware confidence (and the fork: report cards / reweight / store ungraded) is active work.
Static-signal exclusion	Deprivation must be excluded from Monitor change detection so a methodology revision cannot fire a false alert (tracked and assigned).
Billing migration	Underlying catalog still carries older self-serve tiers. New self-serve checkout disabled; fully migrating to the four packages is in progress.
Enterprise security posture	SOC 2 and ISO 27001 not yet in place; status page and formal SLAs need maturing. Procurement gates for the largest buyers.
Proprietary planner, dynamic sources, real-time	NL path still depends on a third-party model; planning apps / EPC / broadband / footfall would enrich the catalog; the clock is monthly where fast sources want event streams.
Calibration & commercial proof	The highest-value model rung is not yet climbed (needs a longer corpus + outcome data); reference logos, case studies, and published pilots are still to come. The company is pre-revenue.
X.7
Part X
The pricing model in detail
The mechanics underneath. Metering: every call emits a usage event; monthly usage is their sum. Quotas: a hard-allowance tier (free Developer) is cut off with a 429 past allowance; a soft-allowance paid tier is allowed to exceed and bills overage. The NL sub-cap: the one call with a real marginal cost has its own tighter monthly cap (10 on the free tier), the specific control that keeps language-model cost bounded. Rate limit: a per-minute cap independent of the monthly quota.

The unit economics. Deterministic calls are nearly free to serve (cached, persisted store; high cache-hit rate at scale). Only the NL path has real marginal cost, and it is capped. The result is an infrastructure-grade margin structure: high gross margin, costs dominated by people and go-to-market rather than per-call compute, and a variable cost that falls to near zero once the proprietary planner replaces the third-party model.

The free tier as a growth loop. A deliberate acquisition channel, not charity. The cost exposure per free developer is tiny and bounded (at most 200 mostly-deterministic calls and 10 language-model calls a month), a rounding error against the value of a developer who pulls their company into a Core API or Decision Intelligence conversation. Making MCP free is what turns “a developer tried it” into “a developer's team is in the funnel.”

The substrate and why demo-led. Billing runs on Stripe, mid-transition from an older self-serve six-tier catalog to the four demo-led packages (new self-serve checkout disabled, existing subscribers grandfathered, retired prices being archived). Regulated, high-ACV buyers do not buy infrastructure from a checkout page; they buy through a workflow conversation, a pilot, and a contract. The free developer-led top of funnel feeds that motion by letting the people who will champion the product internally experience it first, at no cost and no friction.

Part XI
The exhaustive glossary
Address-level
Data at the granularity of an individual property. We are area-level today; address-level is roadmap, and would preserve the no-personal-data posture.
Anomaly
An area behaving unusually versus its peers, measured by a peer-relative z-score. Surfaced by /v1/insights and used by Monitor.
API key
A secret bearer token, prefixed oga_, that authenticates a programmatic caller and ties usage to a customer.
Bundle
A Levers concept: the subset of signals an org's keys are allowed to see and query.
Composite score
The single 0 to 100 number from the Scores product, made of weighted dimensions.
Confidence
A 0 to 1 trust level on a signal or dimension, with a plain-language reason. High ~1.0, medium ~0.7, low ~0.4, none ~0.2.
Corpus
The persisted monthly history of all signals. The moat. Cannot be back-filled.
Data Zone
The Scottish small-area unit (~500–1,000 residents, codes S01), the Scottish equivalent of an LSOA.
Derived signal
A signal we compute from raw signals and history (YoY, trend slope, momentum, peer-relative z-score).
Deterministic
Same input, same output, every time, until a version is deliberately changed.
Dimension
One weighted component of a composite score (e.g. Safety and Crime), with its own sub-score, reasoning, and confidence.
Engine version
The stamped, pinnable version of the scoring methodology (currently v2.0.2), returned on every response and in X-Engine-Version.
ICP
Ideal customer profile: lenders, insurers, CRE, public sector, proptech.
IMD / WIMD / SIMD
The official multiple-deprivation indices for England, Wales, and Scotland. Static signals.
Intelligence
The fourth product: the typed query and insight plane over the corpus. Not a chatbot.
k-NN
k nearest neighbours; the method behind peers: the k most similar areas by normalized-signal distance.
LAD
Local Authority District, the council level of geography; used to scope queries.
Levers
The cross-cutting configuration and lock-in layer: orgs, keys, custom presets and bundles, thresholds, methodology pinning, RBAC, white-label, IP allowlist.
LSOA
Lower-layer Super Output Area, the E&W small-area unit (~1,500 residents, codes E01/W01). The default grain for most data.
MCP
Model Context Protocol; the standard by which AI tools call external tools. Our MCP server exposes the query surface to AI agents.
Metering
The usage-event system that powers billing and the demand-signal moat.
Monitor
The third product: change detection and alerts over a portfolio.
Normalization
Putting a raw signal onto a common 0 to 1 scale so signals can be compared and combined.
Observed period
The time a signal value describes (e.g. Apr 2025 to Mar 2026). What makes the history meaningful.
Peer / peer group
The most similar areas to a target by signal fingerprint, not geography. Stored as a materialised peer graph.
Peer-relative z-score
How far an area sits from its peer group's average on a signal, in standard deviations. The anomaly measure.
Percentile
Where an area ranks on a signal relative to all others (e.g. 38th percentile on crime).
Plan / plan_source
The typed JSON that describes an Intelligence query, the contract; natural language is one way to produce it. plan_source marks whether it came from NL (nl) or was supplied programmatically (client).
Preset
A named weighting of signals for Scores (moving, business, investing, research), or a custom org weighting.
Provenance snapshot
The record written on every ingest (source, release date, ingest time, licence, checksum, row count, notes) that makes a value defensible.
Proxy clamping
Capping a proxy value's confidence so it can never present as high.
Quota / rate limit
A plan's monthly call allowance (with a tighter NL sub-cap), enforced in the request path; the rate limit is a separate per-minute cap.
RBAC
Role-based access control: owner, admin, member roles within an org.
Signal
The atom of the system: a named, addressable fact about an area with a value, unit, direction, source, confidence, and observed period. Signals is also the first product.
signal_values / signal_timeseries
The current-values table and the historical-values table (keyed by observed period). source_snapshots is the provenance table.
Static signal
A signal that changes rarely and only by methodology revision (e.g. deprivation). Must be excluded from change detection.
Trend slope / YoY
The regression slope of a signal over a trailing window (direction and rate of change); year-on-year is a signal's change versus 12 months ago.
Time-series
The monthly history of a signal. See corpus.
End of document · The Master Reference & Playbook · Engine v2.0.2 · Internal study reference

Engine v2.0.2
Internal · study reference