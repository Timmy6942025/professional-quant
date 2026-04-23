# Web Research Protocol - Deep Research Edition

## When Web Research is MANDATORY

You MUST do web research for EVERY analysis unless specifically told not to. Missing recent developments = incomplete analysis.

**Minimum triggers:**
1. Earnings in last 3 months (actual results, not just estimates)
2. Stock moved >5% in last 5 days (find the catalyst)
3. User asks about fundamentals (don't guess, research)
4. Major news events (product launches, regulatory, M&A)
5. Analyst actions (upgrades, downgrades, price targets)
6. Sector rotation events (Fed meetings, economic data)

---

## Deep Research Workflow (The "Insane" Protocol)

### Phase 1: Multi-Source News Scan (10+ sources)

Don't just read one article. Read MULTIPLE sources with different perspectives.

```bash
# Primary news sources to search
websearch("TICKER stock news 2026")
websearch("TICKER earnings results Q1 2026")
websearch("TICKER analyst rating 2026")
websearch("TICKER price target wall street consensus")

# Sentiment/checking for manipulation
websearch("TICKER seeking alpha")
websearch("TICKER bloomberg terminal")
websearch("TICKER reuters")
websearch("TICKER marketwatch")

# Alternative perspectives (contrarian sources)
websearch("TICKER bear case 2026")
websearch("TICKER short interest 2026")
```

### Phase 2: Primary Source Research (Read the actual documents)

**Earnings calls are gold** - don't just read summaries.

```bash
# Earnings call transcripts (full text via webfetch)
webfetch("[URL from earnings call site]")

# SEC filings (raw data)
webfetch("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-K")
webfetch("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-Q")

# Company IR pages (official statements)
webfetch("https://investor.TICKER.com/")
```

### Phase 3: Cross-Verification

**Never trust one source.** Verify with 3+ sources.

```
1. Article says "Beat earnings by $0.23"
   → Cross-check: Was it actually $0.23? (SEC filing, earnings call)

2. "Analyst raised PT to $280"
   → Cross-check: Is this consensus or outlier? (Multiple analyst PTs)

3. "Revenue up 12%"
   → Cross-check: Is this organic or acquisitions? (Segment breakdown)
```

### Phase 4: Timeline Reconstruction

**Map news events to price movements.**

```
Timeline for AMZN:
- Jan 15: "AWS growth accelerates" → Stock up 3% same day
- Feb 2: Earnings beat → Stock up 5% next day
- Feb 20: "Competition from MSFT Azure" → Stock down 2%
- Mar 1: Analyst upgrade to $280 → Stock up 1%

CONCLUSION: News events correlate with price moves. 
Recent catalyst is [most recent news], likely driving current sentiment.
```

### Phase 5: Sentiment Tracking

**How has narrative changed over time?**

```
30 days ago: "AMZN faces antitrust headwinds"
15 days ago: "AMZN wins cloud contract, AWS momentum"
Today: "AMZN AI services driving cloud growth"

SHIFT: Narrative shifted from bearish (regulatory) to bullish (AI/cloud)
This explains why stock is up X% despite [macro headwinds].
```

### Phase 6: Forward-Looking Research

**What's NEXT, not just what happened.**

```bash
# Upcoming catalysts
websearch("TICKER earnings date Q2 2026")
websearch("TICKER product launch 2026")
websearch("TICKER conference presentation 2026")

# Macro factors affecting stock
websearch("Fed meeting date 2026 impact tech stocks")
websearch("tech sector outlook 2026")
websearch("AI spending forecast 2026")

# Risk factors
websearch("TICKER regulatory risk 2026")
websearch("TICKER competition 2026 threat")
```

---

## Source Categories & What to Extract

### Category 1: Earnings & Fundamentals
**What to find:**
- Revenue growth rate (YoY, QoQ)
- EPS actual vs estimated (beat/miss magnitude)
- Guidance changes (raised/lowered/maintained)
- Segment performance (which division driving results)
- Margin trends (expanding/contracting)

**Red flags:**
- "Beat by penny" (barely beat)
- Revenue growth slowing but margins expanding (cost cutting, not growth)
- Guidance raised but stock still down (expectations even higher)

### Category 2: Analyst Actions
**What to find:**
- Price target consensus (high/low/average)
- Recent upgrades/downgrades (who, why)
- Rating distribution (X buy, Y hold, Z sell)
- Key bull arguments (what makes them BUY)
- Key bear arguments (what makes them SELL)

**Check:** Is consensus price target achievable given fundamentals?

### Category 3: News Catalysts
**What to find:**
- Product launches (when, what, market impact)
- M&A activity (acquisitions, partnerships)
- Regulatory changes (headwind or tailwind)
- Leadership changes (CEO/CFO departures)
- Legal issues (lawsuits, investigations)

### Category 4: Market Context
**What to find:**
- Interest rate sensitivity (how will Fed affect this stock)
- Sector rotation (is money flowing in or out of sector)
- Index performance (how does stock compare to SPY/QQQ)
- Correlation breakdown (is this stock moving with or against sector)

### Category 5: Alternative/Critical Perspectives
**What to find:**
- Short seller reports (infer from search: "TICKER short seller")
- Bear cases from contrarian analysts
- Risk factors rarely mentioned in bullish articles
- Insider selling/buying patterns

---

## Integration Into Deep Analysis

### In "Signal Conflict Resolution":
```
"Backtest says BUY (156% return historically) but forecast says SELL 
(RSI=93 overbought). Web research reveals WHY: recent earnings beat 
by 23 cents with raised guidance - fundamental story is strong despite 
overbought technicals. This explains the conflict: technicals show 
short-term overbought, fundamentals show long-term bullish. RESOLUTION: 
BUY on pullback to support, not chase at current levels."
```

### In "Scenario Analysis":
```
"Bull case catalyst: [Specific event from web research, e.g., 
'Analysts expect AWS growth to accelerate to 25% in Q2 2026']

Bear case trigger: [Specific risk from web research, e.g., 
'Regulatory scrutiny of cloud market could limit AMZN pricing power']"
```

### In "Contrarian Perspective":
```
"Consensus is BUY (15 analysts with price targets averaging $280).
However, short interest is X% of float, and web research reveals 
[contrarian concern, e.g., 'competition from MSFT and GOOGL intensifying'].
This creates potential for [specific negative scenario].

What's NOT priced in: [Surprise that could move stock significantly]."
```

---

## Research Quality Checklist

Before finishing web research, verify:
- [ ] Read at least 3 different sources (different perspectives)
- [ ] Read primary source (earnings call transcript, not summary)
- [ ] Cross-verified key facts with 2+ sources
- [ ] Identified the RECENT catalyst (what moved stock recently)
- [ ] Found upcoming catalysts (earnings date, events)
- [ ] Found contrarian perspectives (bear case, risks)
- [ ] Mapped news timeline to price movements
- [ ] Identified what's priced in vs. not priced in
- [ ] Updated scenario probabilities based on research

---

## "Insane" Deep Research Example

```python
# Phase 1: Multi-source scan
websearch("AMZN earnings Q1 2026")
→ Results: Reuters, Bloomberg, Seeking Alpha, Yahoo Finance

websearch("AMZN analyst price target 2026")
→ Results: MS raises to $300, GS stays at $275, BofA at $285

# Phase 2: Primary source
webfetch("https://seekingalpha.com/article/...")
→ Read FULL earnings call transcript
→ Extract: "AWS revenue up 18% YoY, AI services growing faster than expected"

# Phase 3: Cross-verification
Check: "Did AWS really grow 18%?"
→ Verify with SEC 10-Q filing
→ Confirmed: AWS segment shows $XXB revenue, +18% YoY

# Phase 4: Timeline reconstruction
Feb 2: Earnings beat → +5%
Feb 5: MS upgrade to $300 → +2%
Feb 10: "AI competition" article → -1%
Feb 15: Today → Current price reflects all above

# Phase 5: Forward-looking
websearch("AMZN Q2 2026 earnings date")
→ "Expected April 25, 2026"

# Synthesis
"Web research reveals strong AWS fundamentals, multiple analyst 
upgrades, upcoming earnings catalyst. Narrative has shifted from 
'cloud competition concerns' to 'AI-driven growth story'. This 
supports bullish thesis despite overbought RSI. Next catalyst: 
Q2 earnings April 25."
```

---

## Red Flags in Research

**Warning signs that article may be unreliable:**
1. Only cites one source (no cross-verification possible)
2. Uses vague language ("likely", "might", "could") without specifics
3. No mention of risks (overly bullish = suspicious)
4. Predates major events (outdated information)
5. Anonymous sources (can't verify)
6. Sponsored content (not clearly marked)
7. Contradicts SEC filings (someone is lying)

---

## Minimum Standards

**You MUST:**
1. Search at least 3 different sources
2. Fetch at least 1 primary source (earnings transcript, SEC filing)
3. Identify recent catalyst (what moved stock recently)
4. Find upcoming catalysts (earnings date, events)
5. Get analyst consensus (price targets, ratings)
6. Find contrarian view (risks, bear case)
7. Integrate findings into deep analysis sections

**Skip at your own risk:** This is the difference between shallow and "insane" research.
