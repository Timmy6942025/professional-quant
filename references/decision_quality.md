# Decision Quality

## The Goal: Good Decisions, Not Good Outcomes

A good decision can have a bad outcome (you bought at the right price, but a black swan hit). A bad decision can have a good outcome (you gambled and got lucky). Over time, good decisions compound into good results. Bad decisions eventually catch up with you.

**Evaluate your PROCESS, not your outcome.**

---

## When to Pass

The most underrated skill in investing is knowing when NOT to trade.

### Automatic PASS Conditions

| Condition | Why Pass |
|-----------|----------|
| No causal mechanism | You have a feeling, not a thesis |
| No identifiable edge | What you know is already in the price |
| No catalyst | You might be right, but when does the market realize it? |
| No defined stop-loss | Risk is undefined — you can't manage what you can't measure |
| Expected value < friction | The trade costs more than you can reasonably expect to make |
| Key data missing | You're guessing, not analyzing |
| Conflicting signals with no resolution | No edge in confusion |
| Under 1 year of data | Insufficient history for reliable backtesting |
| You changed your mind 3x during analysis | You don't have conviction — you have confusion |

### The "Would I Bet My Portfolio?" Test

Before any trade, ask: "If this were the ONLY position I could take this year, would I still take it?"

If the answer is no — your conviction isn't high enough. Pass or reduce size.

### The "Sleep Test"

"Can I sleep comfortably with this position?" If you'd be checking the stock price at 3am, the position is too big or the thesis is too weak.

---

## Confidence Calibration

### The Calibration Scale

| Level | Meaning | Position Size | Expected Win Rate |
|-------|---------|--------------|-------------------|
| **High (8-10)** | Thesis survived red-team, clear edge, defined catalyst | 5-10% of portfolio | 65-70% |
| **Medium (6-7)** | Decent thesis, some uncertainty, partial edge | 2-5% of portfolio | 55-60% |
| **Low (5)** | Weak thesis, significant unknowns, marginal edge | 1-2% or skip | 50-55% |
| **Below 5** | No edge, unfalsifiable, or opposing case is stronger | 0% — PASS | N/A |

### Confidence Factors

Rate each factor 1-10:

1. **Data quality**: Are the numbers reliable? (yfinance data = 6-7, SEC filings = 9-10)
2. **Causal clarity**: Do I understand the mechanism, or am I pattern-matching?
3. **Edge identification**: Can I articulate what the market is missing?
4. **Catalyst certainty**: Is there a specific event that will cause re-pricing?
5. **Risk definition**: Do I know my maximum loss and what would make me wrong?

**Overall confidence = weighted average, but ANY factor below 5 caps the overall rating at Medium.**

### Common Confidence Errors

| Error | What Happens | Fix |
|-------|-------------|-----|
| **Overconfidence** | High conviction on thin evidence | Require red-team survival for High |
| **Precision illusion** | "Expected return: +14.73%" | Use ranges: "Likely +10-20%" |
| **Anchoring to conviction** | Won't change view despite new evidence | If evidence changes, conviction must change |
| **Social proof** | "Everyone is bullish" = high confidence | Consensus ≠ evidence. Herds can be wrong. |
| **Hindsight confidence** | "I knew it would go up" (after it does) | Record predictions BEFORE outcomes |

---

## Decision Hygiene

### Before the Decision

1. **State your thesis out loud** — If it sounds weak when you say it, it IS weak
2. **Identify the strongest counter-argument** — Can you refute it?
3. **Check for bias** — Are you seeking confirming or disconfirming evidence?
4. **Define the stop-loss** — At what point do you admit you're wrong?
5. **Calculate expected value** — Is the risk/reward favorable?

### During the Decision

- **Don't average conflicting signals** — Resolve them or pass
- **Don't add positions to losing trades** — Average IN to winners, cut losers
- **Don't increase position size because you "feel strongly"** — Feelings aren't evidence
- **Don't skip the red-team because you're in a hurry** — Markets are open tomorrow

### After the Decision

- **Monitor your thesis, not just the price** — Price can move for reasons unrelated to your thesis
- **Re-assess if new information arrives** — Don't hold a thesis that's been invalidated
- **Review your process periodically** — What decisions were good? What were bad? Why?

---

## The Decision Journal

The single most powerful tool for improving decision quality over time.

After every significant analysis, record:

```
DATE: [When]
ASSET: [What]
THESIS: [Your causal argument]
EDGE: [What you think the market is missing]
CATALYST: [What will trigger re-pricing]
KILL SWITCH: [What would make you wrong]
CONVICTION: [High/Medium/Low]
OUTCOME: [Fill in 1-3 months later]
REVIEW: [Was the thesis right? Was the PROCESS right? What would you do differently?]
```

Over time, patterns emerge: You're consistently overconfident on X type of trade, your Y-edge thesis works but your Z-edge thesis doesn't, etc.

**The decision journal converts experience into wisdom.**

---

## Avoiding False Precision

### The Precision Trap

Quantitative tools create an illusion of precision. "Sharpe ratio: 1.83" feels more real than "decent risk-adjusted return." But both are estimates based on historical data, and the future will be different.

**Rules to avoid false precision**:

1. Use ranges, not point estimates: "Expected return: +10-20%" not "+14.73%"
2. Acknowledge model uncertainty: "This backtest assumes future resembles the past — it may not"
3. Round aggressively: "Sharpe ~1.8" not "1.83" — the difference is noise
4. State assumptions: "This estimate assumes margins hold and the Fed doesn't hike"
5. Don't let the number replace the judgment: The number is ONE input, not the answer

### When Numbers Mislead

| Number | What It Seems to Say | What It Might Actually Mean |
|--------|---------------------|----------------------------|
| P/E of 10 | "Cheap" | Value trap if earnings are about to collapse |
| P/E of 50 | "Expensive" | Fair value if earnings will grow 40% for 5 years |
| Sharpe of 2.0 | "Great risk-adjusted return" | Likely overfit — real Sharpe is probably 0.8-1.2 |
| 80% win rate | "High probability strategy" | Survivorship bias — this stock survived; peers didn't |
| +150% backtest return | "Strong strategy" | Regime-dependent — only works in bull markets |
| RSI of 30 | "Oversold" | Getting cheaper for a reason — fundamental deterioration |

**The number is the starting point of analysis, not the conclusion.**

---

## The Art of Saying "I Don't Know"

Three of the most powerful words in investing: **"I don't know."**

Most bad trades come from the inability to admit uncertainty. The pressure to have an opinion on everything is the enemy of good decision-making.

### When to Say "I Don't Know"

- You don't understand the business model
- The data is contradictory and you can't resolve it
- The asset is outside your circle of competence
- The market is behaving irrationally and you can't explain why
- You've researched for an hour and still don't have a thesis

**"I don't know, and I'm going to wait" is a higher-quality decision than "I'll guess bullish."**

---

## Decision Quality Checklist

Before finalizing ANY recommendation:

- [ ] Do I have a causal mechanism (not just a pattern)?
- [ ] Can I articulate my edge (what the market is missing)?
- [ ] Have I sought and addressed the strongest opposing view?
- [ ] Can I state what would change my mind?
- [ ] Is my expected value positive AFTER friction?
- [ ] Is my confidence calibrated to the evidence quality?
- [ ] Am I avoiding false precision?
- [ ] Would I still make this trade if it were my only one this year?
- [ ] Am I making this decision, or is FOMO/emotion making it for me?

**If you can't check all boxes, either reduce size or pass.**

---

## Real-Money Minimum Bar Checklist

Before outputting an Investment Memo with a BUY/SELL/HOLD verdict, verify all of the following:

- [ ] Do I have a Source Ledger with at least 2 primary sources and 1 opposing source, all with dates?
- [ ] Does every major factual claim include the source, date, and specific finding?
- [ ] Does each fact in my Evidence Chain have: Observed → Implies → Matters because?
- [ ] Have I explicitly named my unresolved unknowns and separated tolerable from thesis-breaking?
- [ ] Have I compared this idea to 2-3 peer/alternative opportunities (opportunity cost)?
- [ ] Is my kill-switch a precise condition, not generic concern language?
- [ ] Have I done Research Depth Accounting — what was investigated, resolved, open, and why the recommendation is justified?

**If any box is unchecked, output Research Memo — not Investment Memo.**

Real investment work has texture. A 3-minute answer with no source ledger and no unresolved section is not real investment work — it looks fake, and it is fake. The mode discipline protects both the analyst and the capital.
