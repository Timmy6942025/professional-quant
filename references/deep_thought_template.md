# Deep Thought Template (MANDATORY FILL-OUT)

## Instructions
Before responding to user, you MUST fill out this entire template with specific numbers from script outputs. This is NON-NEGOTIABLE for deep analysis.

---

## Template to Fill Out

### 1. Signal Conflict Resolution
**Script Outputs:**
- Forecast says: [BUY/SELL/HOLD] because [reason from script]
- Backtest says: [STRONG BUY/BUY/SELL/STRONG SELL] because [best strategy + return]
- Risk says: [Risk rating] because [Sharpe/Sortino/Max DD numbers]

**Conflict Analysis (100+ words):**
Why do forecast and backtest disagree? (e.g., "Forecast says SELL because RSI is 93 (overbought), but backtest says STRONG BUY because momentum_20d returned 2156%...")
Which signal is more reliable for this timeframe?
How do I resolve this conflict logically?

### 2. Technical Deep Dive (100+ words)
**RSI Analysis:**
Current RSI: [number]. What does this mean for [TICKER] specifically?
- RSI > 70: Overbought, potential reversal zone
- RSI < 30: Oversold, potential bounce zone
- MY INTERPRETATION: [Your analysis]

**MACD Analysis:**
Current MACD: [number], Signal: [number]
- MACD > Signal: Bullish momentum
- MACD < Signal: Bearish momentum
- MY INTERPRETATION: [Your analysis]

**Moving Average Analysis:**
Price vs SMA 50: [above/below], SMA 50 slope: [rising/falling]
Price vs SMA 200: [above/below], SMA 200 slope: [rising/falling]
Golden Cross? Death Cross? MY INTERPRETATION:

**Bollinger Bands:**
Price relative to bands: [above upper/between/below lower]
Band width: [expanding/contracting] → [volatility expanding/contracting]
MY INTERPRETATION:

### 3. Fundamental Inference (75+ words)
Based on price action and technicals, what might fundamentals look like?
- Why is stock up/down X%?
- What might earnings look like?
- Sector performance suggests [sector context]
- MY SYNTHESIS:

### 4. Risk-Reward Calculus (75+ words)
**Expected Value Calculation:**
- Win probability: X% (based on backtest win rate)
- Win size: X% (average win from risk_metrics.py)
- Loss probability: X% 
- Loss size: X% (average loss from risk_metrics.py)
- Expected Value = (Win% × Win Size) - (Loss% × Loss Size) = X%

**Asymmetric Opportunities:**
- Is there limited downside with unlimited upside?
- What's the risk:reward ratio at current levels?
- MY ANALYSIS:

### 5. Scenario Analysis (100+ words)
**Bull Case (Probability: X%):**
- What needs to happen for stock to reach $X?
- What catalysts could drive this?
- Key inflection points:

**Bear Case (Probability: X%):**
- What could cause -X% drop?
- What risks could materialize?
- Key danger zones:

**Base Case (Probability: X%):**
- Most likely outcome over next 3-6 months:
- Why this scenario is most likely:

**Black Swan Risks:**
- What could go catastrophically wrong?
- Low probability, high impact events:

### 6. Contrarian Perspective (75+ words)
**Consensus View:**
- What is everyone saying about this stock?
- Is the consensus wrong? Why/why not?

**Smart Money Positioning:**
- Based on sector comparison, where might institutions be positioned?
- What's the contrarian play here?

**What's Priced In vs Not:**
- What expectations are already in the price?
- What surprises could move the stock?

### 7. Time Horizon Analysis (50+ words)
- **Short-term (1-30 days)**: Momentum/technicals suggest [direction]
- **Medium-term (1-6 months)**: Fundamentals/sector rotation suggest [direction]  
- **Long-term (6+ months)**: Secular trends suggest [direction]
- **Alignment/Misalignment**: Are all three timeframes aligned?

### 8. Web Research Findings (75+ words)
**Key News (Last 30 Days):**
- [Event] on [Date]: [Impact on price] (Source: websearch/webfetch)
- [Event] on [Date]: [Impact on price] (Source: websearch/webfetch)

**Earnings & Fundamentals:**
- Revenue growth: X% YoY (Source: earnings transcript via webfetch)
- EPS surprise: Beat/Miss by $X (Source: earnings news)
- Guidance: Raised/Maintained/Lowered (Source: analyst report)

**Analyst Sentiment:**
- Price target consensus: $X (Source: Yahoo Finance / Bloomberg)
- Recent upgrades/downgrades: [Details with source]
- Key arguments for: [Bullish points from web research]
- Key arguments against: [Bearish points from web research]

**Upcoming Catalysts:**
- [Event] on [Date]: Potential impact (earnings, FOMC, product launch)
- [Event] on [Date]: Potential impact

**How This Changes My Analysis:**
[Integrate web findings with technical signals, backtest results, risk metrics.
Does web research explain signal conflicts? Does it reveal new risks/opportunities?]

### 9. Final Synthesis (100+ words)
**Key Insights:**
1. 
2. 
3. 

**Thesis Statement (2-3 sentences):**
[Your coherent investment thesis with conviction level]

**Key Risks That Could Invalidate Thesis:**
1. 
2. 
3. 

**Actionable Levels:**
- **Entry Target**: $X.XX (why this level?)
- **Stop Loss**: $X.XX (why this level?)
- **Take Profit 1**: $X.XX (risk:reward 1:2)
- **Take Profit 2**: $X.XX (risk:reward 1:4)

---

## Final Output Structure

After filling out template above, structure your response to user as:

```
## DEEP QUANTITATIVE ANALYSIS: [TICKER]

### Executive Summary
[2-3 sentence thesis with conviction - from Final Synthesis above]

### Signal Analysis  
[From section 1 - Conflict Resolution]

### Technical Deep Dive
[From section 2 - Technical analysis]

### Sector & Peer Context
[From sector_comparison.py output]

### Risk-Reward Profile
[From section 4 - Expected value calculation]

### Scenario Analysis
[From section 5 - Bull/Bear/Base/Black Swan]

### Contrarian Perspective
[From section 6 - What consensus gets wrong]

### Final Verdict
**RECOMMENDATION: [BUY/SELL/HOLD]**
**CONFIDENCE: [HIGH/MEDIUM/LOW]**
**TIME HORIZON: [Short/Medium/Long]**
**KEY RISK: [Single biggest risk]**
**ENTRY TARGET: $X.XX**
**STOP LOSS: $X.XX**
```

**MINIMUM 500 WORDS REQUIRED. NO EXCEPTIONS.**
