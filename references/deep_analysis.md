# Deep Analysis: The Reasoning Operating System

## What Deep Analysis Actually Is

Deep analysis is NOT filling out sections. It's NOT mentioning every indicator. It's NOT writing 1000 words regardless of quality.

**Deep analysis is finding the 2-4 variables that matter most and reasoning about them with causal rigor.**

---

## The Reasoning Hierarchy

### Level 1: Observation (Necessary but Insufficient)
"RSI is 70." "Revenue grew 12%." "The stock is above the 200-day SMA."

Observations are raw data. They're necessary inputs, but they're not analysis. Anyone can read a number off a screen.

### Level 2: Interpretation (Minimum Standard)
"RSI is 70, which historically for THIS stock has meant a 5-10% pullback within 2 weeks 7 out of 10 times."

Interpretation adds context. It connects the observation to historical outcomes. It's analysis, but it's still correlational — it doesn't explain WHY.

### Level 3: Causal Reasoning (The Standard)
"RSI is 70 because the stock rallied 15% in 3 weeks on the back of an earnings beat that raised forward estimates by 8%. The overbought reading reflects genuine fundamental improvement, not speculative excess. In similar situations where RSI is elevated BUT supported by upward estimate revisions, the stock typically continues higher, not lower."

Causal reasoning explains the MECHANISM. It tells you WHY the observation exists and what that means for the future. This is where edge lives.

### Level 4: Second-Order Reasoning (Aspirational)
"RSI is 70 because of the earnings beat. But the earnings beat was driven by a one-time tax benefit that inflated EPS by $0.30, while organic growth actually decelerated from 18% to 14%. The market is celebrating the headline number, but the underlying trend is weakening. When the next quarter shows the organic deceleration, the stock will de-rate. The overbought RSI isn't a technical signal — it's a fundamental mispricing signal."

Second-order reasoning looks BEHIND the apparent cause. It asks: "Is the obvious explanation the REAL explanation?" This is the level that separates good analysts from great ones.

---

## How to Think About Conflicting Signals

### The Wrong Approach: Average Them

"Forecast says BUY, backtest says SELL, sentiment is NEUTRAL → I'll say HOLD."

This is not analysis — it's abdication. You're letting the tools make the decision for you by averaging away the conflict.

### The Right Approach: Resolve Them

1. **WHY do they conflict?** Identify the mechanism behind the disagreement.
   - Different time horizons? (forecast = short-term, backtest = long-term average)
   - Different data inputs? (forecast = price + technicals, backtest = price + volume)
   - Different assumptions? (forecast assumes trend continuation, backtest includes regime changes)

2. **Which signal is more reliable for THIS decision?**
   - If your thesis is about a short-term catalyst → Trust the short-term signal more
   - If your thesis is about a structural shift → Trust the long-term signal more
   - If the conflict is about data quality → Trust the primary source more

3. **Does the conflict reveal something important?**
   - Conflicting signals often point to a transitional period where the old pattern is breaking and a new one is forming
   - This IS the insight — not something to average away, but something to understand

### Conflict Resolution Framework

| Conflict Type | Likely Cause | Resolution |
|---------------|-------------|------------|
| Forecast bullish, backtest bearish | Different time horizons | Which horizon does YOUR thesis address? |
| Technicals bullish, fundamentals weak | Momentum vs value | Is the move backed by fundamentals or speculation? |
| Sentiment bullish, insider selling | Smart money vs crowd | Who is usually right in this situation? |
| Short-term oversold, long-term downtrend | Mean reversion vs trend | Trend > mean reversion in downtrends |
| Backtest strong, but regime changed | Past ≠ future | Does the strategy work in THIS regime? |

---

## How to Connect Qualitative and Quantitative Evidence

### The Integration Mindset

Don't treat qualitative and quantitative as separate tracks that converge at the end. They should inform each other throughout.

- **Qualitative first**: Your understanding of the business, competitive dynamics, and management quality should shape WHICH quantitative tools you use and HOW you interpret their output.
- **Quantitative as test**: Use scripts to test whether the data supports your qualitative thesis.
- **Qualitative as override**: If the numbers say one thing but your qualitative analysis says another, the qualitative usually wins — BUT ONLY if it's evidence-based, not just a feeling.

### Integration Example

**Qualitative thesis**: "This company has a durable moat because of switching costs, and the recent selloff is an overreaction to a temporary headwind."

**Quantitative test**:
- Run `backtest.py` → Does the stock historically recover from similar selloffs?
- Run `fundamentals_screen.py` → Are margins holding despite the headwind?
- Run `earnings_quality.py` → Has management guided for recovery?

**Qualitative override**: If the backtest shows that the stock DOESN'T recover from these selloffs, ask WHY. Is the moat weaker than you thought? Is the headwind not temporary? The qualitative thesis may need revision.

---

## How to Move from Facts to Decision

### The Decision Pipeline

1. **Facts** → What do we know? (Specific numbers, events, data)
2. **Interpretations** → What do the facts mean? (In context, for THIS asset)
3. **Thesis** → What is the causal argument? (Why will price move?)
4. **Edge** → What is the market missing? (Your specific advantage)
5. **Decision** → BUY/SELL/HOLD/WAIT/PASS (Based on edge + risk/reward)
6. **Sizing** → How much? (Based on conviction + risk)
7. **Exit** → When do I change my mind? (Monitoring triggers)

### The Common Mistake: Jumping from Facts to Decision

"RSI is 30 → BUY" skips 5 steps. The correct reasoning is:

"RSI is 30 → [Interpretation] This stock is in a downtrend and RSI 30 is not unusual → [Thesis] The oversold reading does NOT indicate a bottom because the fundamental trend is negative → [Edge] The market is NOT mispricing this — the low RSI reflects real deterioration → [Decision] PASS — no edge in buying a falling knife without a catalyst."

---

## The Importance Hierarchy

Not all analysis sections are equally important. Allocate your effort proportionally.

| Importance | What to Focus On | Why |
|------------|-----------------|-----|
| **Critical** | Causal thesis + Edge + Kill switch | These determine whether you have a trade at all |
| **High** | Key evidence (2-4 facts), Opposing case, Scenario analysis | These determine conviction and sizing |
| **Medium** | Risk/reward, Timeframe alignment, Macro context | These calibrate the decision |
| **Low** | Full indicator rundown, Detailed backtest stats | Supporting context, not decision drivers |

**Spend 70% of your effort on Critical and High items. Don't let the Low-importance items consume your analysis.**

---

## Quality Standards

- **Every claim needs a cause** — Not "the stock will go up" but "the stock will go up BECAUSE [mechanism]"
- **Every signal needs context** — Not "RSI is 70" but "RSI is 70, which for THIS stock has meant [specific historical outcome]"
- **Every conflict needs resolution** — Not "signals are mixed" but "signals are mixed because [reason], and I resolve this by [method]"
- **Every thesis needs a kill switch** — "I am wrong if [specific event]"
- **Every decision needs sizing** — Not just direction, but magnitude based on conviction
- **Every position needs an exit** — Defined before entry, not after
- **No padding** — Don't write 500 words of generic analysis to reach a word count. Write 200 words of insight instead.

**The standard is: would a professional portfolio manager find this analysis decision-useful? If not, rewrite it.**
