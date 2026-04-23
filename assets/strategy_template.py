"""
Template for new trading strategy
"""
import vectorbt as vbt

class StrategyTemplate:
    def __init__(self, ticker, start="2025-01-01", end="2026-04-23"):
        self.ticker = ticker
        self.close = vbt.YahooData.download(ticker, start=start, end=end).get("Close")
    
    def generate_signals(self):
        # TODO: Implement signal logic
        entries = self.close > self.close.rolling(50).mean()
        exits = self.close < self.close.rolling(50).mean()
        return {"entries": entries, "exits": exits}
    
    def backtest(self):
        signals = self.generate_signals()
        return vbt.Portfolio.from_signals(self.close, signals["entries"], signals["exits"])

if __name__ == "__main__":
    strategy = StrategyTemplate("AAPL")
    pf = strategy.backtest()
    print(f"Total Return: {pf.total_return():.2%}")
