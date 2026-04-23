# Portfolio Optimization

## Max Sharpe Ratio
Optimize portfolio to maximize risk-adjusted return
- Implemented in `scripts/portfolio_optim.py` using PyPortfolioOpt

## Min Volatility
Optimize for lowest volatility at a target return
- Modify `scripts/portfolio_optim.py` to use `ef.min_volatility()`

## Equal Weight
Simple allocation: equal weight to all assets
- No optimization needed, just divide 1 by number of tickers

## Efficient Frontier
Set of portfolios with maximum return for a given risk level
- Use `ef.efficient_frontier()` to generate points
