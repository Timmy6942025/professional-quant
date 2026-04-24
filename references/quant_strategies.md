# Quant Strategies (Free, No API Key)

> **Role in this skill**: Appendix — implementation details for when you decide to test a specific strategy. These are NOT the starting point of analysis. Form your thesis first (see `references/thesis_first.md`), then use these strategies to test it. Strategies are hypothesis testers, not thesis generators.

## SMA Crossover
- Enter when fast SMA > slow SMA, exit when fast < slow
- Use `scripts/backtest.py` to test (default parameters: 50/200 SMA)

## Momentum
- Buy assets with positive N-day returns, sell those with negative returns
- Implement with vectorbt: Calculate rolling returns, generate entry/exit signals

## Mean Reversion
- Buy when price < lower Bollinger Band, sell when > upper band
- Calculate bands: `df['Close'].rolling(20).mean() ± 2*df['Close'].rolling(20).std()`

## Pairs Trading (Stat Arb)
- Trade two correlated stocks: long underperformer, short outperformer
- Calculate spread: `spread = price_a - beta * price_b`
- Enter when spread deviates > 2 std from mean
