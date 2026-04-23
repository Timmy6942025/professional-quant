# Deep Analysis Guidelines - MANDATORY

## CRITICAL: Deep Thinking Protocol

You MUST think deeply about every aspect of the analysis. This is not optional. Shallow analysis = useless analysis.

---

## Step 1: Run All Scripts (EXACT ORDER)

Execute in order, wait for each to complete:
1. `python3 scripts/fetch_data.py TICKER` - Get raw data (2+ years minimum)
2. `python3 scripts/forecast.py TICKER` - Get price prediction + technical signals
3. `python3 scripts/backtest.py TICKER` - Get strategy backtest results
4. `python3 scripts/risk_metrics.py TICKER` - Get comprehensive risk profile
5. `python3 scripts/sector_comparison.py TICKER --peers ...` - Compare to sector
6. `python3 scripts/news_sentiment.py TICKER` - Get news sentiment
7. `python3 scripts/master_analysis.py TICKER` - Get final aggregated verdict

**Record ALL outputs** - you need specific numbers for analysis.

---

## Step 2: DEEP ANALYTICAL THINKING (Minimum 1000 words)

After running scripts, you MUST produce deep analysis covering ALL sections below:

### A. Signal Conflict Resolution (CRITICAL)

**Never average conflicting signals - RESOLVE them.**

1. List EVERY signal from every script (forecast, backtest, risk, sentiment, sector)
2. Identify which signals CONFLICT (e.g., forecast SELL vs backtest STRONG BUY)
3. Explain WHY conflict exists using specific mechanisms:
   - "Forecast says SELL because RSI=93 (overbought) but backtest says BUY because momentum_20d returned 2156% historically when RSI was elevated but MACD was bullish"
   - "Risk metrics show HIGH risk (Sharpe=0.8) but backtest shows 156% return - WHY? Because Sharpe is based on volatility, not direction. High volatility ≠ losing money"
4. WEIGH signals by reliability for THIS timeframe:
   - Short-term (1-30 days): Technicals > Fundamentals > Backtest
   - Long-term (6+ months): Fundamentals > Backtest > Technicals
5. Make a DECISION - don't waffle with "could be either"

### B. Technical Deep Dive (Stock-specific)

**Generic RSI analysis = lazy. Analyze THIS stock.**

For EACH indicator, answer:
1. What does this indicator mean SPECIFICALLY for THIS stock?
2. What historical context exists? (e.g., "AMZN RSI hit 93 in Jan 2024 and dropped 15%")
3. Is current reading at an EXTREME or moderate level?
4. What does divergence/convergence with price suggest?

Indicators to analyze:
- RSI: Overbought/oversold, divergence from price, rising/falling trend
- MACD: Crossover, histogram slope, signal strength
- Bollinger Bands: Position (%B), bandwidth (volatility), squeeze detection
- Moving Averages: 20/50/200 SMA alignment, golden/death cross history
- Volume: Price-volume divergence, volume profile, institutional flow
- Support/Resistance: Key levels, breakouts, fakeouts

### C. Fundamental Inference from Price Action

**Don't have fundamentals? INFER them from price.**

- Why is stock up X% YTD? What narrative supports this?
- Is price movement backed by fundamentals or speculation?
- What does P/E expansion vs contraction suggest about expectations?
- Sector context: How does this stock compare to sector ETF performance?
- Interest rate sensitivity: Is this a growth stock sensitive to rates?

### D. Risk-Reward Calculus (ACTUAL NUMBERS)

**Calculate expected value, not just feelings.**

```
Expected Value = (Win Probability × Win Size) - (Loss Probability × Loss Size)

Example:
- Backtest win rate: 62% → Win Probability = 0.62
- Average win: 15% → Win Size = 0.15
- Average loss: -8% → Loss Size = 0.08
- Loss Probability: 38% → 1 - 0.62 = 0.38

EV = (0.62 × 0.15) - (0.38 × 0.08)
EV = 0.093 - 0.030
EV = 0.063 = 6.3% expected return per trade
```

Also analyze:
- Asymmetric payoff: Is upside 3x downside?
- Max drawdown: Can you handle -45% peak-to-trough?
- Sharpe ratio interpretation: Is 1.5 good for THIS volatility regime?

### E. Scenario Analysis with PROBABILITIES

**Every scenario needs a probability and catalyst.**

| Scenario | Probability | Catalyst | Target | Timeframe |
|----------|-------------|----------|--------|----------|
| Bull | 30% | [What drives this?] | $XXX | X months |
| Base | 50% | [Most likely path] | $XXX | X months |
| Bear | 15% | [What triggers drop?] | $XXX | X months |
| Black Swan | 5% | [Tail risk] | $XXX | Any |

For each scenario answer:
- What NEEDS to happen for this scenario to occur?
- What events would INVALIDATE this scenario?
- Where is the "line in the sand" that changes everything?

### F. Contrarian Thinking (What Consensus Gets Wrong)

**Challenge every assumption.**

1. What is the consensus view on this stock?
2. Is the consensus RIGHT or WRONG? (Be specific)
3. Where is smart money positioned? (Long? Short? Flat?)
4. What's PRICED IN that everyone knows?
5. What's NOT PRICED IN that could surprise?
6. What would make you WRONG? (Define your "out")

### G. Time Horizon Alignment

**Are all timeframes aligned or conflicting?**

| Horizon | Signal | Conviction |
|---------|--------|------------|
| Short (1-30 days) | [Momentum direction] | High/Med/Low |
| Medium (1-6 months) | [Fundamental direction] | High/Med/Low |
| Long (6+ months) | [Secular trend] | High/Med/Low |

**Critical**: If timeframes conflict, identify WHICH one drives current price action.

### H. Macro-Micro Linkage

**How do macro forces affect THIS stock?**

For each relevant macro factor:
- Fed policy: Rate hikes/cuts → Impact on this stock
- Dollar strength: USD up/down → Impact on this stock
- Sector rotation: Risk-on/risk-off → Impact on this stock
- Economic data: CPI/jobs → Impact on this stock
- Geopolitical: War/trade → Impact on this stock

### I. Edge Case & Tail Risk Identification

**What could go catastrophically wrong?**

1. Chart patterns suggesting topping formation?
2. Fundamental risks not in consensus view?
3. Black swan scenarios (war, pandemic, regulatory)?
4. Liquidity risks if market drops?
5. Correlation breakdown risks?

---

## Step 3: Output Structure (MANDATORY)

```
## DEEP QUANTITATIVE ANALYSIS: [TICKER]

### Executive Summary (2-3 sentences)
[Clear thesis with conviction level]

### Signal Analysis [Conflict Resolution]
[Explain why signals agree/disagree, which is most reliable]

### Technical Deep Dive
[Indicator-by-indicator analysis for THIS stock]

### Fundamental Inference
[What price action tells us about fundamentals]

### Risk-Reward Profile
[Expected value calculation, asymmetric opportunities]

### Scenario Analysis
[Bull/Base/Bear/Black Swan with probabilities]

### Contrarian Perspective
[What consensus misses]

### Macro-Micro Linkage
[How macro affects this stock specifically]

### Final Verdict
**RECOMMENDATION: [BUY/SELL/HOLD]**  
**CONFIDENCE: [HIGH/MEDIUM/LOW]**  
**TIME HORIZON: [Short/Medium/Long]**  
**KEY RISK: [Single biggest risk]**  
**ENTRY TARGET: $X.XX**  
**STOP LOSS: $X.XX**  
**UPSIDE: X% | DOWNSIDE: X%**  
**RISK:REWARD: 1:X**
```

---

## Thinking Standards

- **Minimum 1000 words** of analysis (not counting script output)
- **Every section MUST be filled** - no skipping
- **Specific numbers from scripts** in all reasoning
- **No hedging language** - "might", "could", "possibly" = weak
- **Probabilistic thinking** - "60% likely" not "will go up"
- **Stock-specific analysis** - not generic "RSI overbought"
- **Resolve conflicts** - don't average, decide
- **Define your "out"** - what makes you wrong?
