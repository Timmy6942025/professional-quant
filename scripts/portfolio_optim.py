#!/usr/bin/env python3
import yfinance as yf
import argparse
from pypfopt import EfficientFrontier, risk_models, expected_returns
import numpy as np

def optimize_portfolio_comprehensive(tickers, start="2020-01-01", end="2026-04-23"):
    # Download data
    df = yf.download(tickers, start=start, end=end, progress=False)["Close"]
    if isinstance(df, pd.Series):
        df = df.to_frame()
    
    # Calculate expected returns and covariance
    mu = expected_returns.mean_historical_return(df)
    S = risk_models.sample_cov(df)
    
    print(f"\n{'='*70}")
    print(f"PORTFOLIO OPTIMIZATION")
    print(f"{'='*70}")
    
    results = {}
    
    # Strategy 1: Max Sharpe
    ef_sharpe = EfficientFrontier(mu, S)
    ef_sharpe.max_sharpe()
    weights_sharpe = ef_sharpe.clean_weights()
    perf_sharpe = ef_sharpe.portfolio_performance(verbose=False)
    results['Max_Sharpe'] = {
        'weights': weights_sharpe,
        'return': perf_sharpe[0] * 100,
        'volatility': perf_sharpe[1] * 100,
        'sharpe': perf_sharpe[2]
    }
    
    # Strategy 2: Min Volatility
    ef_minvol = EfficientFrontier(mu, S)
    ef_minvol.min_volatility()
    weights_minvol = ef_minvol.clean_weights()
    perf_minvol = ef_minvol.portfolio_performance(verbose=False)
    results['Min_Volatility'] = {
        'weights': weights_minvol,
        'return': perf_minvol[0] * 100,
        'volatility': perf_minvol[1] * 100,
        'sharpe': perf_minvol[2]
    }
    
    # Strategy 3: Efficient Return (target 15% return)
    try:
        ef_effret = EfficientFrontier(mu, S)
        ef_effret.efficient_return(0.15)
        weights_effret = ef_effret.clean_weights()
        perf_effret = ef_effret.portfolio_performance(verbose=False)
        results['Efficient_15pct'] = {
            'weights': weights_effret,
            'return': perf_effret[0] * 100,
            'volatility': perf_effret[1] * 100,
            'sharpe': perf_effret[2]
        }
    except:
        pass
    
    # Find best strategy
    best_strategy = max(results.items(), key=lambda x: x[1]['sharpe'])
    
    # Output
    print(f"\nOPTIMIZATION RESULTS:")
    print(f"\n{'Strategy':<20} {'Return':>10} {'Volatility':>12} {'Sharpe':>10}")
    print(f"{'-'*70}")
    for name, data in results.items():
        print(f"{name:<20} {data['return']:>9.2f}% {data['volatility']:>11.2f}% {data['sharpe']:>10.2f}")
    
    print(f"\n{'='*70}")
    print(f"BEST STRATEGY: {best_strategy[0]}")
    print(f"Expected Return: {best_strategy[1]['return']:.2f}%")
    print(f"Volatility: {best_strategy[1]['volatility']:.2f}%")
    print(f"Sharpe Ratio: {best_strategy[1]['sharpe']:.2f}")
    
    print(f"\nOPTIMAL WEIGHTS:")
    for ticker, weight in best_strategy[1]['weights'].items():
        print(f"  {ticker}: {weight*100:.2f}%")
    
    # Risk assessment
    if best_strategy[1]['sharpe'] > 1.5:
        assessment = "EXCELLENT - High return, controlled risk"
    elif best_strategy[1]['sharpe'] > 1.0:
        assessment = "GOOD - Solid risk-adjusted returns"
    elif best_strategy[1]['sharpe'] > 0.5:
        assessment = "ACCEPTABLE - Moderate risk-adjusted returns"
    else:
        assessment = "POOR - Low risk-adjusted returns, reconsider allocation"
    
    print(f"\nASSESSMENT: {assessment}")
    print(f"{'='*70}\n")
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comprehensive portfolio optimization")
    parser.add_argument("tickers", nargs="+", help="Stock tickers (e.g., AAPL MSFT)")
    parser.add_argument("--start", default="2020-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", default="2026-04-23", help="End date (YYYY-MM-DD)")
    args = parser.parse_args()
    
    import pandas as pd
    optimize_portfolio_comprehensive(args.tickers, args.start, args.end)
