# Model Pitfalls

## Overfitting
Model works on training data, fails on new data
- Fix: Walk-forward validation, simplify model, reduce features

## Lookahead Bias
Using future data to make predictions (e.g., using 2026 data for 2025 forecasts)
- Fix: Lag all features, never use future data in training

## Survivorship Bias
Only including currently listed stocks, ignoring delisted stocks
- Fix: Use total return indices, include delisted assets if possible

## Data Snooping
Testing multiple strategies on same data, leading to false positives
- Fix: Use out-of-sample data for final validation

## Transaction Costs
Ignoring fees, slippage
- Fix: Include fees in backtests (vectorbt `fees` parameter)
