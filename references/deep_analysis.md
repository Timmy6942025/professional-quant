# Deep Analysis Guidelines - MANDATORY

## CRITICAL: Deep Thinking Protocol

You MUST think deeply about every aspect of the analysis. This is not optional.

### Step 1: Run All Scripts
Execute in order:
1. `python3 scripts/fetch_data.py TICKER` - Get raw data
2. `python3 scripts/forecast.py TICKER` - Get price prediction + technical signals
3. `python3 scripts/backtest.py TICKER` - Get strategy backtest results
4. `python3 scripts/risk_metrics.py TICKER` - Get comprehensive risk profile
5. `python3 scripts/master_analysis.py TICKER` - Get final verdict

### Step 2: DEEP ANALYTICAL THINKING (Minimum 500 words)

After running scripts, you MUST produce deep analysis covering:

#### A. Signal Conflicts & Synthesis
- Identify ALL conflicting signals between forecast, backtest, and risk
- Explain WHY conflicts exist (e.g., "Forecast says SELL but backtest says STRONG BUY because...")
- Resolve conflicts with logical reasoning, not averaging
- Weigh signals by reliability (backtest > forecast > risk for long-term, inverse for short-term)

#### B. Technical Deep Dive
- Analyze RSI: What does 93.08 (overbought) mean for AMZN specifically?
- Analyze MACD: Bullish crossover but is momentum sustainable?
- Analyze Bollinger Bands: Price position relative to bands, volatility compression/expansion
- Analyze volume patterns: Is price movement supported by volume?
- Analyze moving average alignment: Golden cross? Death cross?

#### C. Fundamental Context (Inferred)
- Based on price action, what might fundamentals look like?
- Sector performance: Compare to SPY, QQQ, sector ETFs
- Market regime: Bull, bear, or transition? How does this affect signals?
- Interest rate sensitivity: Tech stocks like AMZN are rate-sensitive

#### D. Risk-Reward Calculus
- Calculate expected value: (Probability of win * Win size) - (Probability of loss * Loss size)
- Analyze max drawdown tolerance: Can portfolio withstand -56% drawdown?
- Sharpe/Sortino interpretation: What do these numbers mean in practice?
- Asymmetric opportunities: Where is payoff asymmetric (limited downside, unlimited upside)?

#### E. Scenario Analysis
- Bull case: What needs to happen for AMZN to reach forecast price?
- Bear case: What could cause -30% drawdown?
- Base case: Most likely outcome with probability
- Black swan risks: What could go catastrophically wrong?

#### F. Contrarian Thinking
- What is the consensus view? Is it wrong?
- Where is smart money likely positioned?
- What's priced in vs. what's not?
- What would change your mind? (Identify key inflection points)

#### G. Time Horizon Analysis
- Short-term (1-30 days): Momentum, technicals dominate
- Medium-term (1-6 months): Fundamentals, sector rotation
- Long-term (6+ months): Secular trends, business model

#### H. Final Synthesis
- Combine ALL above into single coherent thesis
- State conviction level with reasoning
- Identify key risks that could invalidate thesis
- Provide actionable entry/exit levels

### Step 3: Output Format

Structure your response:

```
## DEEP QUANTITATIVE ANALYSIS: [TICKER]

### Executive Summary
[2-3 sentence thesis with conviction level]

### Signal Analysis
[Conflict resolution, synthesis of all scripts]

### Technical Deep Dive
[Detailed chart analysis, indicator interpretation]

### Risk-Reward Profile
[Expected value, asymmetric opportunities, drawdown analysis]

### Scenario Analysis
[Bull/Bear/Base cases with probabilities]

### Contrarian Perspective
[What consensus gets wrong]

### Final Verdict
**REC.MMENDATION: [BUY/SELL/HOLD]**
**CONFIDENCE: [HIGH/MEDIUM/LOW]**
**TIME HORIZON: [Short/Medium/Long]**
**KEY RISK: [Single biggest risk]**
**ENTRY TARGET: $X.XX**
**STOP LOSS: $X.XX**
```

## Thinking Requirements

- Minimum 500 words of analysis AFTER running scripts
- Never skip any section above
- Use specific numbers from script outputs in your reasoning
- Question every signal - don't accept blindly
- Think like a portfolio manager, not a script monkeys
