# Professional-Quant Skill

A deep market intelligence skill for AI agents. **Thesis-driven analysis, not script orchestration.** Decisive conclusions, no disclaimers.

**Always uses current date automatically** (`datetime.now()`) — never hallucinates dates. **Full yfinance access** — 24 scripts powered by free, no-API-key market data.

---

## What This Skill Does

Most quant skills run scripts and average the signals. This one **thinks first**.

The agent forms a causal thesis about what drives an asset, researches what matters, self-verifies by building the opposing case, then uses quantitative tools to challenge or sharpen its view. Scripts are sanity checks and measurement tools — not substitutes for reasoning.

**Result**: Analysis that identifies the 2-4 variables that matter, explains the causal mechanism, states what would change its mind, and delivers a decisive BUY / SELL / HOLD / WAIT / PASS verdict with calibrated confidence.

---

## The Reasoning Loop

Every analysis follows this process:

1. **Orient** — What is this asset? What drives it? What regime is it in?
2. **Build thesis** — A specific, falsifiable causal claim (not a feeling)
3. **Identify unknowns** — The 2-4 things you need to know but don't
4. **Targeted research** — Find the decisive variable, not 10 articles saying the same thing
5. **Test with scripts** — Run the scripts relevant to YOUR thesis (not all of them)
6. **Red-team** — Steel-man the opposing case, find your weakest evidence
7. **Reconcile** — Does the opposing case change your thesis?
8. **Decide or pass** — BUY / SELL / HOLD / WAIT / PASS (passing is a valid answer)
9. **Set monitoring triggers** — What specific event would change your mind?

---

## What Makes This Different

| Traditional Quant Skill | Professional-Quant |
|------------------------|-------------------|
| Run all scripts, average signals | Form thesis first, use scripts to test it |
| "RSI 70 = overbought" | "Earnings decelerating while multiples expand — the market is pricing in a re-acceleration that may not happen" |
| Cover every indicator | Identify the 2-4 variables that drive 80% of the outcome |
| List pros and cons, hedge | Steel-man the opposition, then take a position or pass |
| "Expected return: +14.73%" | "Likely +10-20% — range, not false precision" |
| "Consult a financial advisor" | Deliver conviction or say "no edge — pass" |
| Equities only | Equities, indices, commodities, FX, rates, crypto, special situations |

---

## Asset Coverage

Not just stocks. The skill adapts its framework across asset types:

- **Equities** — Earnings, moats, management, capital allocation
- **Indices / ETFs** — Concentration risk, breadth, factor rotation
- **Commodities** — Supply/demand, capital cycle, cost curves
- **FX** — Rate differentials, central bank policy, carry dynamics
- **Rates / Bonds** — Duration, credit, yield curve shape
- **Crypto** — Adoption, reflexivity, on-chain data, narrative
- **Special Situations** — M&A arb, spinoffs, restructuring, legal catalysts

Each asset type has a dedicated playbook with primary drivers, key questions, research priorities, and common pitfalls. See `references/asset_playbooks.md`.

---

## Scripts & Data (yfinance-Powered)

24 Python scripts providing free, no-API-key market data and analysis via **yfinance**:

### Core Scripts
| Script | Purpose |
|--------|---------|
| `fetch_data.py` | 2+ years OHLCV via yfinance |
| `forecast.py` | Prophet forecast + RSI/MACD/Bollinger Bands |
| `backtest.py` | Strategy returns vs Buy & Hold (annualized alpha) |
| `risk_metrics.py` | Sharpe, Sortino, VaR, Beta, Max Drawdown |
| `master_analysis.py` | Aggregated signal synthesis (run last as cross-check) |

### Context Scripts
| Script | Purpose |
|--------|---------|
| `sector_comparison.py` | Relative strength vs peers/ETF |
| `news_sentiment.py` | News bullish/bearish scoring |
| `macro_analysis.py` | VIX, rates (TLT), dollar (UUP) |
| `fundamentals_screen.py` | P/E, P/B, debt/equity, margins |
| `earnings_quality.py` | Beat/miss rates, earnings manipulation flags |
| `regime_detector.py` | Bull/bear/sideways market detection |

### Advanced Scripts
| Script | Purpose |
|--------|---------|
| `portfolio_optimizer.py` | Efficient frontier, max Sharpe, risk parity |
| `correlation_matrix.py` | Pairwise correlations, ASCII heatmap |
| `sector_rotation.py` | Sector momentum signals |
| `insider_tracker.py` | Insider ownership/sentiment |
| `short_squeeze.py` | Short interest, squeeze potential |
| `options_analysis.py` | IV, put/call, gamma exposure |
| `kelly_sizer.py` | Kelly Criterion position sizing |
| `sec_filings.py` | 10-K/10-Q SEC EDGAR access |
| `multi_timeframe.py` | Daily/Weekly/Monthly alignment |
| `multi_stock_compare.py` | Side-by-side comparison |
| `fibonacci_levels.py` | Retracement/extension levels |
| `volume_profile.py` | VWAP, POC, value area |
| `technical_alerts.py` | Breakout/breakdown detection |

All scripts use `datetime.now()` — no hardcoded dates. All backtests enforce **strict quant rules**: no look-ahead bias, mandatory friction (fees + slippage), correct compounding, and sanity check tripwires.

---

## Reference Library (19 Files)

The skill includes a deep reference library organized by purpose:

### Core Reasoning (Load First)
- `thesis_first.md` — How to build a thesis before touching tools
- `self_verification.md` — Iterative red-team and revision protocol
- `qualitative_mosaic.md` — Non-numeric analysis lenses (moats, management, regulation, supply chain)
- `research_for_edge.md` — Insight-seeking research protocol
- `decision_quality.md` — When to pass, confidence calibration, decision hygiene
- `asset_playbooks.md` — Framework adaptation for each asset type

### Deep Analysis Guidance
- `deep_analysis.md` — Reasoning operating system (how to think, not what to fill out)
- `deep_thought_template.md` — Analysis workbench (iterative thesis pad, NOT a mandatory form)
- `web_research.md` — Research for decisive information

### Mental Models & Wisdom
- `cognitive_biases.md` — Biases that destroy returns + pre-trade checklist
- `market_wizards.md` — Trading legend principles as thinking prompts
- `what_changes_everything.md` — How to find the one fact that matters most
- `advanced_techniques.md` — Reflexivity, narrative, crowding, second-order effects
- `price_action.md` — Technical analysis depth (a sub-tool, not the worldview)

### Reference & Appendix
- `financial_metrics.md` — Metric definitions (lookup, not reading)
- `quant_strategies.md` — Strategy implementation details (hypothesis testers, not thesis generators)
- `model_pitfalls.md` — Overfitting, false precision, tool overreliance, cognitive traps
- `portfolio_optimization.md` — Optimization methods, Kelly sizing, regime-aware construction
- `data_sources.md` — What data is available, what's not, and how to bridge the gaps

---

## Install

Copy-paste this prompt into **any AI agent** (OpenCode, kilo code, Codex, etc.) to install the skill:

```
Clone the professional-quant skill from https://github.com/Timmy6942025/professional-quant and set it up in my .agents directory so it works immediately.

Steps:
1. git clone https://github.com/Timmy6942025/professional-quant.git ~/.agents/skills/professional-quant
2. pip3 install --break-system-packages yfinance vectorbt prophet PyPortfolioOpt numpy pandas ruff
3. Confirm the skill is installed by checking if ~/.agents/skills/professional-quant/SKILL.md exists.

Then tell me "Skill installed. Ready for deep market analysis."
```

**OpenCode users** can also run:
```bash
opencode install professional-quant
```

---

## Update

When you make changes to the repo, users can update with one command:
```bash
# Option 1: Run the update script (easiest)
~/.agents/skills/professional-quant/update-skill.sh

# Option 2: Direct git pull
cd ~/.agents/skills/professional-quant && git pull

# Option 3: Re-install fresh (if issues)
git clone https://github.com/Timmy6942025/professional-quant.git ~/.agents/skills/professional-quant --force
```

---

## After Installation

Ask your agent:
```
Analyze AAPL stock and tell me if I should invest.
```

The agent will follow the reasoning loop: orient → build thesis → research → test with scripts → red-team → decide. You'll get a decisive BUY/SELL/HOLD/WAIT/PASS verdict with calibrated confidence, key evidence, the opposing case, and monitoring triggers. No disclaimers.

Or try a non-equity asset:
```
What's the outlook for gold (GLD) over the next 6 months?
```

```
Should I be in long-duration bonds (TLT) right now?
```

---

## Code Quality & CI

All scripts pass `ruff` linting and formatting with a security-focused configuration.

```bash
# Check for lint issues
cd ~/.agents/skills/professional-quant && ruff check scripts/

# Auto-fix trivial lint issues
ruff check scripts/ --fix

# Check formatting (dry run)
ruff format --check scripts/

# Apply formatting
ruff format scripts/
```

A **CI workflow** (`.github/workflows/lint.yml`) runs `ruff check`, `ruff format --check`, and `pytest` on every push and PR to `main`. All must pass before merging.

---

## Repository

https://github.com/Timmy6942025/professional-quant
