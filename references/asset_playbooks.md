# Asset Playbooks

## Purpose

The analysis framework applies to ANY asset, but the questions that matter, the signals that work, and the research priorities change dramatically by asset type. This file provides mini-playbooks for each major asset class.

You are NOT limited to equities. You are a general market thinker.

---

## Equities (Individual Stocks)

### Primary Drivers
- Earnings growth trajectory
- Margin structure and direction
- Capital allocation (buybacks, dividends, M&A, R&D)
- Competitive position and moat durability
- Management credibility and alignment

### Key Questions
- Is the moat real? Has it been tested?
- Is management trustworthy? Do they eat their own cooking?
- What is the margin of safety at this price?
- Is the earnings growth organic or financial engineering?
- What would cause a de-rating (multiple compression)?

### Research Priority
1. Earnings call transcripts (management tone, guidance credibility)
2. Segment-level performance (which division is driving results?)
3. Competitive dynamics (market share data, pricing trends)
4. Balance sheet strength (debt maturity, covenants, refinancing risk)
5. Insider activity (are they buying or selling?)

### Scripts Most Useful
`fetch_data.py`, `forecast.py`, `backtest.py`, `risk_metrics.py`, `fundamentals_screen.py`, `earnings_quality.py`

### Common Pitfalls
- Confusing a good company with a good stock (overpaying for quality)
- Ignoring capital allocation (great business, terrible management)
- Anchoring to purchase price (price doesn't care about your cost basis)
- Survivorship bias in backtests (this stock survived — what about peers that didn't?)

---

## Indices & ETFs (Market-Level Analysis)

### Primary Drivers
- Concentration risk (how much does the top 5-10 drive performance?)
- Macro regime (is it a risk-on or risk-off environment?)
- Leadership breadth (are a few stocks carrying the index, or is participation broad?)
- Factor rotation (growth vs value, large vs small, quality vs momentum)
- Liquidity conditions (is money flowing in or out?)

### Key Questions
- How concentrated is this index? What happens if the top 3 stumble?
- Is market breadth expanding or contracting?
- Which sectors are leading? Does leadership suggest continuation or reversal?
- Is equal-weight outperforming cap-weight? (Sign of breadth)
- What is the macro regime, and which factors benefit?

### Research Priority
1. Index composition and concentration (top 10 weight, sector weight)
2. Advance/decline line and breadth indicators
3. Factor performance (value, growth, quality, momentum, size)
4. Fund flows (is money moving in or out of this asset class?)
5. Macro data (employment, inflation, PMI, policy)

### Scripts Most Useful
`macro_analysis.py`, `sector_rotation.py`, `regime_detector.py`, `correlation_matrix.py`

### Common Pitfalls
- Assuming index = diversified (S&P 500 is ~30% Magnificent 7)
- Ignoring concentration risk in cap-weighted indices
- Not understanding what's INSIDE the ETF (holdings, weighting)
- Assuming past index performance reflects future potential (survivorship bias)

---

## Commodities

### Primary Drivers
- Supply/demand balance (inventory levels, production capacity)
- Cost curve position (where is marginal production?)
- Geopolitical supply risk (war, sanctions, OPEC decisions)
- Capital cycle (are producers investing or cutting capex?)
- USD strength (commodities priced in dollars)
- Seasonal patterns (refinery maintenance, planting season, heating demand)

### Key Questions
- Where are we in the capital cycle? (Under-invested = bull, over-invested = bear)
- Is there a supply response coming? How long does it take to bring new supply online?
- What is the inventory situation? (Above or below 5-year average?)
- What does the cost curve look like? (What price makes marginal production unprofitable?)
- Is this a structural trend or a cyclical blip?

### Research Priority
1. Inventory data (EIA, LME, USDA depending on commodity)
2. Production data and capacity utilization
3. Capital expenditure trends (are producers investing or cutting?)
4. Geopolitical risk assessment
5. Substitution economics (at what price do alternatives become viable?)

### Scripts Most Useful
`fetch_data.py` (for commodity ETFs), `regime_detector.py`, `macro_analysis.py`

**Note**: Scripts are less useful for commodities. Manual reasoning and supply/demand analysis are primary. Use scripts for context on commodity ETFs, not for direct commodity analysis.

### Common Pitfalls
- Confusing price with value (commodities don't have cash flows — price IS the fundamental)
- Ignoring the capital cycle (every high price plants the seeds of oversupply)
- Assuming past supply disruptions will repeat
- Forgetting that commodity producers are NOT the commodity (miner ≠ gold)

---

## FX (Foreign Exchange)

### Primary Drivers
- Interest rate differentials (carry trade dynamics)
- Real rate differentials (nominal rates minus inflation)
- Central bank policy divergence (who's hiking, who's cutting?)
- Trade balance and current account flows
- Capital flows (FDI, portfolio flows, safe haven demand)
- Geopolitical positioning (reserve currency status, sanctions)

### Key Questions
- What does the central bank WANT? (Is the currency too strong or too weak for their goals?)
- Are real rates attractive? (Is the yield worth the risk after inflation?)
- Is there policy divergence that creates a carry opportunity?
- What are capital flows doing? (Is money moving toward or away from this currency?)
- Is this a trend trade or a mean-reversion trade?

### Research Priority
1. Central bank minutes and statements (policy direction)
2. Interest rate differentials and forward curves
3. Inflation data and real rate calculation
4. Trade balance and current account trends
5. Positioning data (COT reports, if available)

### Scripts Most Useful
`macro_analysis.py` (for rate/UUP context), `regime_detector.py`

**Note**: FX analysis is primarily macro-driven. Scripts are supplementary — use them for context on USD environment and rate trends.

### Common Pitfalls
- Thinking in nominal rates instead of real rates
- Ignoring central bank intervention (they can and do move markets)
- Overcomplicating (FX is often driven by 1-2 variables)
- Forgetting that FX is a RELATIVE game (every currency trade is a pair)

---

## Rates (Bonds / Fixed Income)

### Primary Drivers
- Central bank policy rate and forward guidance
- Inflation expectations (breakeven rates)
- Real yields (nominal minus expected inflation)
- Credit risk (for corporate bonds)
- Duration exposure (sensitivity to rate changes)
- Supply/demand for bonds (issuance, central bank buying/selling)

### Key Questions
- Where are we in the rate cycle? (Hiking, pausing, or cutting?)
- What is the market pricing in for the next meeting? (Is that too much or too little?)
- Are real yields positive or negative? (Positive = attractive for lenders)
- What is the term premium doing? (Is the market demanding compensation for duration risk?)
- Is the yield curve inverted? (Historical recession signal)

### Research Priority
1. Central bank statements and minutes
2. Inflation data and forecasts (CPI, PCE, breakevens)
3. Yield curve shape and term premium
4. Credit spreads (for corporate bonds)
5. Issuance calendar and supply/demand dynamics

### Scripts Most Useful
`macro_analysis.py` (TLT/UUP context), `risk_metrics.py`

**Note**: Rate analysis is almost entirely macro-driven. Scripts provide context on the current rate environment only.

### Common Pitfalls
- Confusing yield with return (price changes can overwhelm yield)
- Ignoring duration risk (long bonds move a lot for small rate changes)
- Assuming the curve will normalize on your timeline
- Forgetting that bond markets are smarter than equity markets about macro

---

## Crypto

### Primary Drivers
- Liquidity conditions (global money supply, risk appetite)
- Adoption curves (users, transactions, TVL for DeFi)
- Reflexivity (price increase → media attention → new buyers → price increase)
- Regulation (government stance, ETF approvals, enforcement)
- Narrative and sentiment (crypto is narrative-driven more than most assets)
- Technical structure (halving cycles, token release schedules, staking yields)

### Key Questions
- Is this genuine adoption or speculative froth?
- What triggers the reflexivity loop — and what breaks it?
- Is there a structural catalyst (ETF approval, institutional entry, technology milestone)?
- What is the regulatory risk? Could government action materially affect this?
- What does the on-chain data say about holder behavior?

### Research Priority
1. On-chain analytics (holder distribution, exchange flows, active addresses)
2. Adoption metrics (users, transactions, merchant acceptance)
3. Regulatory developments (legislation, enforcement, ETF approvals)
4. Macro liquidity conditions (M2 growth, risk appetite)
5. Narrative analysis (what story is driving interest right now?)

### Scripts Most Useful
Limited. `macro_analysis.py` for liquidity context, `regime_detector.py` for market regime

**Note**: Crypto analysis is heavily qualitative and narrative-driven. Scripts provide macro context only. Manual reasoning is primary.

### Common Pitfalls
- Treating crypto like equities (no cash flows, no earnings, different valuation framework)
- Ignoring reflexivity (crypto is MORE reflexive than any other asset class)
- Assuming past cycle patterns will repeat (each cycle has unique characteristics)
- Confusing technology value with token value (great protocol ≠ valuable token)
- Underestimating regulatory risk (governments can and do restrict access)

---

## Special Situations (Event-Driven)

### Primary Drivers
- Catalyst path and timeline (what event, when, and what's the probability?)
- Legal/regulatory clarity (what are the hurdles and how likely are they to clear?)
- Information asymmetry (do you know something the market doesn't about the outcome?)
- Timeline risk (how long until resolution? Can you afford to wait?)
- Structural edge (is there a forced seller, a arbitrage opportunity, a dislocation?)

### Key Questions
- What is the probability-weighted outcome across all scenarios?
- What is the timeline to resolution?
- What are the key legal/regulatory milestones?
- Is there a structural reason the market is mispricing this?
- What happens if the deal/event DOESN'T happen? (Downside protection)

### Types of Special Situations

| Type | Key Variable | Edge Source |
|------|-------------|-------------|
| M&A arbitrage | Deal probability + timeline | Regulatory analysis, synergy assessment |
| Spinoff | Sum-of-parts discount | Neglected subsidiary, forced selling |
| Restructuring | Recovery value | Creditor analysis, asset valuation |
| Legal/regulatory | Outcome probability | Precedent analysis, expert assessment |
| Distressed debt | Recovery rate | Asset valuation, capital structure |
| Post-earnings drift | Earnings surprise magnitude | Estimate revision dynamics |

### Research Priority
1. Legal/regulatory documents (filings, court records, agency statements)
2. Timeline analysis (when are the key decision points?)
3. Precedent research (what happened in similar situations?)
4. Structural analysis (who is forced to sell/buy and why?)
5. Downside protection (if the event doesn't happen, what's the loss?)

### Scripts Most Useful
`risk_metrics.py`, `fundamentals_screen.py`

**Note**: Special situations are primarily legal/timeline/structural analysis. Scripts are marginally useful.

### Common Pitfalls
- Overestimating deal probability (deals fail more often than you think)
- Ignoring timeline risk (the market can stay irrational longer than you can stay solvent)
- Not having a "deal breaks" downside case
- Confusing a special situation with a regular investment

---

## Cross-Cutting Principles

Regardless of asset type, these principles apply:

1. **Identify the 1-2 variables that matter most** — Don't spread attention across 20 factors
2. **Know what regime you're in** — The same signal means different things in different environments
3. **Have a thesis before using tools** — Scripts test your view, they don't create it
4. **Research for decisive information** — Find the fact that resolves the key uncertainty
5. **Self-verify before concluding** — Build the opposing case, test your weakest assumption
6. **Pass if no edge** — Not every asset deserves a trade
