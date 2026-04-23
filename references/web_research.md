# Web Research Protocol for Deep Analysis

## When to Use Web Research

**MANDATORY for every analysis:**
1. Recent earnings releases (last 3 months)
2. Major news events affecting stock price
3. Sector-wide events (rate changes, regulation, etc.)
4. Analyst upgrades/downgrades
5. Upcoming catalysts (earnings dates, product launches, FOMC meetings)

## Web Research Workflow

### Step 1: Search Recent News (Last 30 Days)
Use websearch tool with these queries:

```
"TICKER stock news 2026"
"TICKER earnings Q1 2026"
"TICKER analyst rating upgrade downgrade"
"TICKER price target Wall Street"
```

### Step 2: Sector/Market Context
```
"tech sector outlook 2026" (for tech stocks)
"Fed interest rates 2026 impact stocks"
"market regime 2026 bull bear"
```

### Step 3: Company-Specific Deep Dives
```
"TICKER AWS growth 2026" (for AMZN)
"TICKER AI strategy 2026" (for tech)
"TICKER competition 2026"
```

### Step 4: Read Key Articles with webfetch
When websearch returns URLs, use webfetch to read full articles:
- Earnings call transcripts
- Analyst reports (seeking alpha, motley fool)
- SEC filing summaries
- Major news from Reuters/AP/Bloomberg

## What to Extract from Web Research

### Earnings & Fundamentals
- Revenue growth rate (YoY)
- EPS surprises (beat/miss)
- Guidance raised/lowered
- Margin trends (expanding/contracting)

### News Catalysts
- Product launches
- Mergers & acquisitions
- Regulatory changes
- Leadership changes (CEO/CFO)
- Partnerships/collaborations

### Analyst Sentiment
- Price targets (high/low/consensus)
- Rating changes (buy/sell/hold)
- Key arguments for/against

### Market Context
- Interest rate sensitivity
- Sector rotation trends
- Geopolitical risks
- Consumer spending trends

## Integrating Web Research into Deep Analysis

### In "Signal Conflict Resolution" Section:
"Web research reveals [specific event] happened on [date], explaining why backtest (which uses historical data) says BUY but forecast (which sees current overbought conditions) says SELL..."

### In "Fundamental Inference" Section:
"Web research shows:
- Revenue grew X% YoY (source: earnings call)
- Analyst consensus price target: $X (source: Yahoo Finance)
- Recent upgrade from MS to BUY (source: Bloomberg)
This suggests fundamentals support [bullish/bearish] thesis..."

### In "Scenario Analysis" Section:
"Bull case catalyst: [upcoming event from web research]
Bear case catalyst: [risk factor from web research]"

### In "Contrarian Perspective" Section:
"Consensus view is [bullish/bearish] based on [web finding].
However, [contrarian insight from deep research] suggests..."

## Search Tips for Better Results

### Use Year + Quarter Specifics
- "Q1 2026" not just "recent"
- "April 2026" for timely results

### Search Multiple Sources
- Search: "TICKER seeking alpha"
- Search: "TICKER reuters"
- Search: "TICKER bloomberg"
- Compare narratives across sources

### Verify with Primary Sources
- Don't just trust headlines
- Use webfetch to read actual earnings transcripts
- Check company IR page for official statements

## Red Flags to Watch For

When doing web research:
1. **Pump and dump articles** - Overly promotional, no risks mentioned
2. **Outdated information** - News from 6 months ago that's priced in
3. **Conflicting narratives** - Dig deeper to find truth
4. **Paid promotions** - Clearly sponsored content
5. **Clickbait headlines** - Read full article, not just title

## The "Insane" Deep Research Edge

What separates shallow web search from insane deep research:

1. **Primary source obsession** - Read earnings transcripts, not summaries
2. **Cross-verification** - Check 3+ sources before believing
3. **Timeline reconstruction** - Map news events to price movements
4. **Sentiment tracking** - How did narrative change over time?
5. **Future-looking** - What's NEXT, not just what happened

## Example Deep Research for AMZN

```
websearch("AMZN earnings Q1 2026")
→ Found: "Amazon beats EPS by $0.23, revenue up 12%"

websearch("AMZN AWS growth 2026")
→ Found: "AWS growth accelerates to 18%, AI services driving demand"

websearch("AMZN analyst price target 2026")
→ Found: "15 analysts raise PT to $280, citing AI momentum"

webfetch("https://www.reuters.com/...") [from search result]
→ Read full earnings call transcript

Synthesis: "Web research reveals AWS accelerating (18% growth), 
AI services gaining traction. 15 analysts raised PT to $280.
This supports STRONG BUY thesis from backtest, despite 
overbought RSI. The fundamental story overrides technicals."
```

## Mandatory Integration

**Add to deep_thought_template.md section:**
```
### 9. Web Research Findings (75+ words)
**Key News (Last 30 Days):**
- [Event] on [Date]: [Impact on price]
- [Event] on [Date]: [Impact on price]

**Earnings & Fundamentals:**
- Revenue growth: X% YoY
- EPS surprise: Beat/Miss by $X
- Guidance: Raised/Maintained/Lowered

**Analyst Sentiment:**
- Price target consensus: $X
- Recent upgrades/downgrades: [Details]

**Upcoming Catalysts:**
- [Event] on [Date]: Potential impact
- [Event] on [Date]: Potential impact

**How This Changes My Analysis:**
[Integration with technical signals, scenario analysis, etc.]
```
