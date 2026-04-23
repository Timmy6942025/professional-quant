# Deep Thought Template (MANDATORY FILL-OUT)

## Instructions
Before responding to user, you MUST fill out this entire template with specific numbers from script outputs. This is NON-NEGOTIABLE for deep analysis. Minimum 1000 words of written analysis.

---

## Pre-Analysis: Record Script Outputs

### Script: fetch_data.py
```
Date Range: [start] to [end]
Current Price: $X.XX
52-Week Range: $X.XX - $X.XX
Average Volume: X.XM
```

### Script: forecast.py
```
RSI: X.XX (overbought/oversold/neutral)
MACD: X.XX (signal line: X.XX)
Signal: [BULLISH/BEARISH/NEUTRAL]
Prophet Forecast 30d: $X.XX (X% from current)
Prophet Forecast 90d: $X.XX (X% from current)
```

### Script: backtest.py
```
Best Strategy: [SMA_CROSS/RSI_STRAT/MOMENTUM]
Total Return: X.XX%
Win Rate: XX%
Sharpe Ratio: X.XX
Max Drawdown: -XX%
```

### Script: risk_metrics.py
```
Sharpe Ratio: X.XX
Sortino Ratio: X.XX
Beta: X.XX
Max Drawdown: -XX%
VaR (95%): -X%
Calmar Ratio: X.XX
```

### Script: sector_comparison.py
```
Sector ETF: [SPY/QQQ/etc]
Relative Strength: [Outperforming/Underperforming]
Correlation: X.XX
```

### Script: news_sentiment.py
```
Sentiment Score: X.XX (bullish/bearish/neutral)
Key Headlines: [list 3]
```

---

## Section 1: Signal Conflict Resolution (200+ words)

### 1.1 List All Signals
```
Forecast Signal: [BUY/SELL/HOLD] - Reason: [from script output]
Backtest Signal: [STRONG BUY/BUY/SELL/STRONG SELL] - Reason: [from script]
Risk Signal: [LOW/MEDIUM/HIGH RISK] - Reason: [from script]
Sentiment Signal: [BULLISH/BEARISH/NEUTRAL] - Reason: [from script]
Sector Signal: [OUTPERFORMING/UNDERPERFORMING] - Reason: [from script]
```

### 1.2 Identify Conflicts (Be specific)
```
Conflict #1: [Forecast says X but backtest says Y]
WHY this conflict exists: [Detailed explanation with mechanism]
- Forecast uses [technical indicators] which show [current condition]
- Backtest uses [historical data] which shows [long-term pattern]
- These disagree because [specific reason]

Conflict #2: [If exists]
WHY this conflict exists: [Detailed explanation]
```

### 1.3 Resolve Conflicts (DECIDE, don't average)
```
For SHORT-TERM (1-30 days):
The most reliable signal is [X] because [reason with specificity]
My decision: [BUY/SELL/HOLD]

For LONG-TERM (6+ months):
The most reliable signal is [X] because [reason]
My decision: [BUY/SELL/HOLD]
```

---

## Section 2: Technical Deep Dive (200+ words)

### 2.1 RSI Analysis (THIS stock)
```
Current RSI: [number]
RSI Context: [Historical high/low for THIS stock, not generic]
What this RSI level has meant historically for [TICKER]:
[Specific example: "When AMZN RSI hit 93 in Jan 2024, it dropped 15% within 2 weeks"]
MY INTERPRETATION: [Detailed analysis of what RSI suggests for THIS stock]
Signal: [Bullish/ Bearish/ Neutral]
```

### 2.2 MACD Analysis
```
MACD Line: [number]
Signal Line: [number]
MACD Histogram: [positive/negative], [increasing/decreasing]
Crossover occurred: [date], type: [bullish/bearish crossover]
Momentum Assessment: [Is this sustainable? What typically follows?]
Signal: [Bullish/Bearish/Neutral]
```

### 2.3 Moving Average Analysis
```
Price vs SMA 20: [above/below] by X%
SMA 20 trend: [rising/falling/flat]
Price vs SMA 50: [above/below] by X%
SMA 50 trend: [rising/falling/flat]
Price vs SMA 200: [above/below] by X%
SMA 200 trend: [rising/falling/flat]
Golden/Death Cross: [Yes/No], occurred [date]
Overall Trend: [Strong Up/Up/Neutral/Down/Strong Down]
```

### 2.4 Bollinger Bands Analysis
```
Price Position: [above upper band/between bands/below lower band]
Band Width: [expanding/contracting]
BB Width %: [X% - higher = more volatile]
Squeeze Status: [Imminent/Squeeze/Expansion]
Volatility Signal: [Bullish/Bearish/Neutral]
```

### 2.5 Volume Analysis
```
Current Volume: [X] vs Average: [Y]
Volume Trend: [Increasing/Decreasing/Stable]
Price-Volume Relationship: [Price up on high volume = strong / etc]
Institutional Flow Signal: [Accumulating/Distributing/Neutral]
```

### 2.6 Support/Resistance
```
Key Resistance Levels: [List with prices]
Key Support Levels: [List with prices]
Current Position: [Approaching resistance/from support/mid-range]
Breakout Potential: [Upward/Downward/Range-bound]
```

---

## Section 3: Fundamental Inference (150+ words)

### 3.1 Price Action Story
```
Stock is [up/down] X% [YTD/in 6 months/in 1 month]
What narrative explains this move: [Detailed explanation]
Is this move justified by fundamentals or speculation? [Analysis]
```

### 3.2 Sector Context
```
Sector Performance: [X% YTD vs stock at X%]
Relative Strength: [Outperforming/Underperforming by X%]
Sector Rotation Context: [Risk-on/risk-off, growth/value shift]
```

### 3.3 Macro Sensitivity
```
Interest Rate Sensitivity: [High/Medium/Low]
[If tech/growth]: How would Fed rate changes affect this stock?
Dollar Sensitivity: [How does USD strength/weakness affect this?]
```

---

## Section 4: Risk-Reward Calculus (150+ words)

### 4.1 Expected Value Calculation
```
From backtest:
- Win Rate: XX% → Win Probability = 0.XX
- Average Win: X% → Win Size = 0.XX
- Average Loss: -X% → Loss Size = 0.XX
- Loss Probability: XX% → 0.XX

EV = (Win% × Win Size) - (Loss% × Loss Size)
EV = (0.XX × 0.XX) - (0.XX × 0.XX)
EV = X.X%

Interpretation: [Positive/Negative] expected return [per trade/year]
```

### 4.2 Asymmetric Opportunities
```
Upside Scenario: X% potential gain
Downside Scenario: -X% potential loss
Risk:Reward Ratio: 1:X
Is payoff asymmetric? [Yes/No] - [Explanation]
```

### 4.3 Drawdown Tolerance
```
Historical Max Drawdown: -XX%
Can typical portfolio withstand -XX%? [Yes/No]
Recovery time from max DD: [X months]
```

---

## Section 5: Scenario Analysis (200+ words)

### 5.1 Bull Case
```
Probability: XX%
Price Target: $XXX (+XX%)
Timeframe: X months
What needs to happen: [Specific catalysts]
Key support: [Levels that must hold]
Invalidation: [What would prove this wrong]
```

### 5.2 Bear Case
```
Probability: XX%
Price Target: $XXX (-XX%)
Timeframe: X months
What triggers this: [Specific risks]
Key support to break: [Price levels]
Invalidation: [What would prove this wrong]
```

### 5.3 Base Case
```
Probability: XX%
Price Target: $XXX (+/-XX%)
Timeframe: X months
Most likely path: [Detailed scenario]
Why this is most likely: [Specific reasoning]
```

### 5.4 Black Swan
```
Probability: X% (Low but cannot ignore)
Trigger: [Specific event that would cause catastrophe]
Potential Drop: [-XX% to -XX%]
Hedge: [How to protect against this]
```

---

## Section 6: Contrarian Thinking (150+ words)

### 6.1 Consensus View
```
What is Wall Street saying? [Analyst consensus, sentiment]
Is consensus RIGHT or WRONG? [Specific analysis]
Why might consensus be wrong: [Detailed contrarian argument]
```

### 6.2 Smart Money Positioning
```
Based on [sector flows/volume/institutional activity]:
Institutional positioning likely: [Long/Short/Flat]
Smart money entry zones: [$X - $X]
```

### 6.3 What's Priced In vs Not
```
Already priced in: [What everyone knows and has bid in]
Not priced in: [Potential surprises that could move stock]
Upside surprises possible: [Catalysts not in price]
Downside surprises possible: [Risks not fully priced]
```

### 6.4 My "Out" (What makes me wrong)
```
I will be wrong if: [Specific conditions that invalidate thesis]
Key level that proves thesis wrong: $XXX
This would cause me to: [Change recommendation]
```

---

## Section 7: Time Horizon Analysis (100+ words)

### 7.1 Horizon Alignment
```
Short-term (1-30 days): [Direction] - Signal: [technical/momentum]
Medium-term (1-6 months): [Direction] - Signal: [fundamentals/sector]
Long-term (6+ months): [Direction] - Signal: [secular trends/business]

Alignment Status: [All aligned / Mixed / Conflicting]

If conflicting, which timeframe dominates CURRENT price action: [X]
Why: [Specific reasoning]
```

---

## Section 8: Web Research Findings (150+ words)

### 8.1 Recent News (Last 30 Days)
```
[Event 1]: [Date] - [Impact] (Source: [URL])
[Event 2]: [Date] - [Impact] (Source: [URL])
[Event 3]: [Date] - [Impact] (Source: [URL])
```

### 8.2 Earnings & Fundamentals
```
Revenue Growth: XX% YoY (Source: [Earnings call/SEC filing])
EPS: Beat/Miss by $X (Source: [Earnings report])
Guidance: Raised/Maintained/Lowered (Source: [Earnings call])
Key metrics to watch: [List]
```

### 8.3 Analyst Sentiment
```
Price Target Consensus: $XXX (Range: $XXX - $XXX)
Recent changes: [Upgrades/Downgrades details]
Bull case: [Key arguments]
Bear case: [Key arguments]
```

### 8.4 Upcoming Catalysts
```
[Catalyst 1]: [Date] - [Potential impact]
[Catalyst 2]: [Date] - [Potential impact]
[Catalyst 3]: [Date] - [Potential impact]
```

### 8.5 How Web Research Changes Analysis
```
[Does web research support or contradict script outputs?]
[Does it explain signal conflicts?]
[Does it reveal new risks or opportunities?]
```

---

## Section 9: Final Synthesis (200+ words)

### 9.1 Key Insights (3-5 bullet points)
```
1. [Most important insight from analysis]
2. [Second most important]
3. [Third most important]
4. [Risk that concerns me most]
5. [Opportunity I see]
```

### 9.2 Thesis Statement
```
[2-3 sentence coherent investment thesis]
Conviction Level: [HIGH/MEDIUM/LOW] - Why: [Specific reasoning]
```

### 9.3 Key Risks That Could Invalidate Thesis
```
1. [Risk 1]: [Specific condition that would prove thesis wrong]
2. [Risk 2]: [Specific condition that would prove thesis wrong]
3. [Risk 3]: [Specific condition that would prove thesis wrong]
```

### 9.4 Actionable Levels
```
Entry Target: $XXX (Why this level: [Reasoning])
Stop Loss: $XXX (Why this level: [Reasoning])
Take Profit 1: $XXX (Risk:Reward 1:2)
Take Profit 2: $XXX (Risk:Reward 1:4)
Time Horizon: [Short/Medium/Long]
```

---

## Final Output to User

After filling template, present to user in this structure:

```
## DEEP QUANTITATIVE ANALYSIS: [TICKER]

### Executive Summary
[From section 9.2]

### Signal Analysis
[From section 1]

### Technical Deep Dive
[From section 2]

### Fundamental Inference
[From section 3]

### Risk-Reward Profile
[From section 4]

### Scenario Analysis
[From section 5]

### Contrarian Perspective
[From section 6]

### Time Horizon Analysis
[From section 7]

### Web Research Integration
[From section 8]

### Final Verdict
**RECOMMENDATION: [BUY/SELL/HOLD]**  
**CONFIDENCE: [HIGH/MEDIUM/LOW]**  
**TIME HORIZON: [Short/Medium/Long]**  
**KEY RISK: [Single biggest risk]**  
**ENTRY TARGET: $XXX**  
**STOP LOSS: $XXX**  
**UPSIDE: +XX% | DOWNSIDE: -XX%**  
**RISK:REWARD: 1:X**
```

---

## Quality Standards

- **Minimum 1000 words** of written analysis (not counting this template)
- **Every section MUST be filled** - no skipping, no N/A
- **Specific numbers from scripts** - "RSI=93" not "RSI is high"
- **Stock-specific analysis** - "For AMZN, RSI 93 means..." not generic
- **Resolve conflicts** - make a decision, don't average signals
- **Probabilistic** - "60% likely" not "will go up"
- **Define your out** - what makes thesis wrong
