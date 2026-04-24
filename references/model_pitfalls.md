# Pitfalls: Quantitative, Cognitive, and Analytical

## Beyond Overfitting

The original pitfalls (overfitting, lookahead bias, survivorship bias, data snooping, transaction costs) are important for backtests. But the BIGGEST pitfalls in investment analysis aren't mathematical — they're cognitive. They affect every analysis you do, whether or not you run a single script.

---

## The Universal Pitfalls

### 1. False Precision

**The trap**: "The model says the stock will be at $187.42 in 90 days." That number feels precise, so it feels accurate. But the confidence interval on any forecast is enormous. $187.42 ± $40 is probably the real range.

**How to avoid it**:
- Always think in ranges, not point estimates
- Round aggressively: "approximately $185-190" not "$187.42"
- When a script gives you 4 decimal places, mentally truncate to 1-2
- Ask: "What's the 80% confidence interval?" If you can't answer, the point estimate is meaningless
- The more precise a number looks, the more suspicious you should be

**The deeper issue**: False precision creates false confidence. It makes you feel like you know more than you do. The honest answer "I don't know with any precision" is more valuable than a precise wrong number.

### 2. Narrative Fallacy

**The trap**: After the fact, everything seems inevitable. "Of course NVDA went up — AI was the biggest trend of the decade!" But in 2022, the same people were saying "Of course NVDA crashed — crypto mining demand collapsed!"

**How to avoid it**:
- Before forming a narrative, write down 3 alternative explanations that are equally plausible
- Ask: "If the opposite had happened, could I construct an equally compelling narrative?"
- Be suspicious of stories that feel too clean — reality is messy
- The best thesis is one that survived a genuine attempt to disprove it, not one that fits a neat story

### 3. Confirmation Bias

**The trap**: You form a view, then selectively attend to evidence that supports it while dismissing contradicting evidence. This is the default mode of human cognition — it takes active effort to overcome.

**How to avoid it**:
- ALWAYS steel-man the opposing view before finalizing your thesis (see `self_verification.md`)
- When you find confirming evidence, ask: "How many places did I look before finding this?"
- When you find disconfirming evidence, give it 3x the weight of confirming evidence
- Actively search for the strongest counter-argument, not just the first one
- The goal is not to be "balanced" — it's to be CORRECT, which requires genuinely testing your view

### 4. Anchoring

**The trap**: The first number you see becomes an anchor that distorts all subsequent judgment. If the stock is at $150, you anchor there. If someone says "fair value is $200," that becomes a new anchor.

**How to avoid it**:
- Estimate fair value BEFORE looking at the current price
- Think in terms of intrinsic value range, not relative to current price
- "The stock is down 50%" is irrelevant — what matters is whether it's cheap at THIS price
- Don't let the purchase price or the 52-week high influence your assessment of value

### 5. Tool Overreliance

**The trap**: You run 7 scripts and feel like you've done deep analysis. But scripts only measure what's measurable — they can't assess management quality, competitive dynamics, regulatory risk, or industry inflection points. The qualitative factors often matter MORE than the quantitative ones.

**How to avoid it**:
- Scripts are sanity checks, not the analysis itself
- Before running scripts, form a thesis (see `thesis_first.md`)
- After running scripts, ask: "What important factors are NOT captured in any of these outputs?"
- The most valuable analysis is often what the scripts CAN'T tell you
- If all your evidence comes from scripts, you're not thinking — you're just computing

### 6. Recency Bias

**The trap**: The most recent data point feels most important. A stock that just dropped 20% feels "risky." A stock that just rose 20% feels "strong." But the recent move may be noise.

**How to avoid it**:
- Always look at multiple timeframes (1 month, 6 months, 1 year, 3 years, 5 years)
- Ask: "Is this recent move consistent with the long-term trend, or a deviation from it?"
- Don't overweight the last earnings report — look at the trend of earnings
- The market's memory is shorter than yours should be

### 7. Availability Bias

**The trap**: Vivid, recent events feel more important and more probable than they actually are. A dramatic crash makes future crashes feel likely. A recent boom makes future booms feel likely.

**How to avoid it**:
- Base probabilities on base rates, not on how easily examples come to mind
- "How often does this type of event actually happen?" not "How vividly can I imagine it happening?"
- Check historical frequency before estimating probability
- The most likely scenario is often the most boring one

### 8. Sunk Cost

**The trap**: "I've already spent 30 minutes analyzing this stock — I should have a conclusion." No. If the analysis doesn't support a clear conclusion, the correct answer is PASS. Time spent does not create an obligation to trade.

**How to avoid it**:
- The question "Should I buy/sell this?" can always be answered with "No"
- If conviction isn't there after thorough analysis, that IS the answer
- More analysis doesn't always create more clarity — sometimes it creates more confusion
- See `decision_quality.md` for when to pass

---

## Backtest-Specific Pitfalls (Still Important)

### Overfitting
Fitting parameters to historical noise rather than signal. If a strategy has 8+ optimized parameters, it's almost certainly overfit.

**Detection**: Strategy performs well in-sample but fails out-of-sample. Walk-forward testing reveals the decay.

### Lookahead Bias
Using future information in historical analysis. The most insidious form: using data that wasn't actually available at the time (e.g., revised earnings data, survivor-only databases).

**Detection**: If your backtest returns exceed ~30% annually with low drawdown, you probably have lookahead bias. Check every data point: was this actually knowable at this time?

### Survivorship Bias
Analyzing only stocks/companies that survived. Delisted companies, bankrupt firms, and failed funds disappear from databases, making averages look better than reality.

**Detection**: Compare results with and without survivorship-adjusted data. Use point-in-time databases when available.

### Data Snooping
Testing many hypotheses on the same dataset and reporting only the "best" result. If you test 100 strategies, ~5 will look significant at p<0.05 by pure chance.

**Detection**: Apply Bonferroni correction. Use separate in-sample and out-of-sample periods. Be suspicious of strategies that were "discovered" after testing many variants.

### Transaction Costs Underestimation
Backtests often use unrealistic cost assumptions. Real-world costs include: bid-ask spread, market impact (especially for larger orders), opportunity cost of unfilled orders, borrow costs for shorts.

**Detection**: Double your assumed friction. If the strategy still works, it might be real. If it doesn't, it was marginal.

---

## The Meta-Pitfall: Knowing About Biases Doesn't Eliminate Them

Reading this list creates a false sense of immunity. "I know about confirmation bias, so I won't fall for it." Wrong. Knowing about a bias reduces it by maybe 10-20%. The remaining 80-90% still affects you.

**The only reliable defense**: Structured process. Using checklists, red-team protocols, pre-registration of hypotheses, and mandatory steel-manning. Discipline > Awareness.

See also:
- `self_verification.md` — The red-team protocol for actively combating biases
- `thesis_first.md` — Pre-registering your thesis before data mining
- `decision_quality.md` — Process-based decision hygiene
