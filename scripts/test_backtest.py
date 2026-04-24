#!/usr/bin/env python3
"""Unit tests for backtest.py core functions."""

import numpy as np
import pandas as pd
import pytest

from backtest import (
    EXCHANGE_FEE,
    MAX_LEVERAGE,
    SLIPPAGE,
    annualized_return,
    apply_friction,
    calculate_log_returns,
)


# ---------------------------------------------------------------------------
# annualized_return
# ---------------------------------------------------------------------------


class TestAnnualizedReturn:
    """Tests for annualized_return() — CAGR conversion."""

    def test_zero_return(self):
        """0% total return over any period = 0% annualized."""
        assert annualized_return(0, 5) == 0.0

    def test_positive_return_one_year(self):
        """Over exactly 1 year, annualized equals total return."""
        assert annualized_return(50.0, 1) == pytest.approx(50.0)

    def test_positive_return_multi_year(self):
        """100% total over 2 years = ~41.4% annualized (sqrt(2)-1)*100."""
        result = annualized_return(100.0, 2)
        assert result == pytest.approx((2**0.5 - 1) * 100, rel=1e-6)

    def test_aapl_like_scenario(self):
        """Simulate AAPL: 277.66% total over 6.3 years."""
        result = annualized_return(277.66, 1585 / 252)
        # (1 + 2.7766)^(1/6.29) - 1 ≈ 0.2354 → ~23.5%
        assert 22 < result < 25

    def test_negative_return(self):
        """-50% total over 2 years."""
        result = annualized_return(-50.0, 2)
        # (1 - 0.5)^0.5 - 1 = sqrt(0.5) - 1 ≈ -29.3%
        assert result == pytest.approx((0.5**0.5 - 1) * 100, rel=1e-6)

    def test_small_positive_return(self):
        """5% total over 0.5 years = higher annualized."""
        result = annualized_return(5.0, 0.5)
        # (1.05)^2 - 1 ≈ 10.25%
        assert result == pytest.approx((1.05**2 - 1) * 100, rel=1e-6)

    def test_zero_years_returns_input(self):
        """years=0 should return the raw total (guard against div-by-zero)."""
        assert annualized_return(100.0, 0) == 100.0

    def test_negative_years_returns_input(self):
        """Negative years is invalid; should return raw total."""
        assert annualized_return(50.0, -1) == 50.0

    def test_total_loss_minus_100_returns_input(self):
        """-100% total return (total loss) is a degenerate case."""
        assert annualized_return(-100.0, 5) == -100.0

    def test_beyond_total_loss_returns_input(self):
        """Below -100% is impossible; return raw value."""
        assert annualized_return(-150.0, 5) == -150.0

    def test_alpha_calculation(self):
        """Alpha = strategy_annualized - buy_hold_annualized."""
        bh_ann = annualized_return(277.66, 1585 / 252)
        strat_ann = annualized_return(97.16, 1585 / 252)
        alpha = strat_ann - bh_ann
        # Alpha should be a reasonable negative number, not -180%
        assert -20 < alpha < -5
        # Specifically, should NOT be the old buggy -180%
        assert alpha > -50

    def test_same_return_different_years(self):
        """Same total return over longer period = lower annualized."""
        ann_2yr = annualized_return(100.0, 2)
        ann_5yr = annualized_return(100.0, 5)
        assert ann_2yr > ann_5yr


# ---------------------------------------------------------------------------
# calculate_log_returns
# ---------------------------------------------------------------------------


class TestCalculateLogReturns:
    """Tests for calculate_log_returns()."""

    def test_basic_returns(self):
        """Simple price series with constant position=1."""
        close = pd.Series([100, 110, 121])
        positions = pd.Series([1.0, 1.0, 1.0])
        log_rets, _cumulative = calculate_log_returns(close, positions)
        # Log returns: ln(110/100), ln(121/110)
        expected_log = np.log(close / close.shift(1))
        pd.testing.assert_series_equal(log_rets, positions.shift(1) * expected_log)

    def test_zero_position_no_return(self):
        """Position=0 should produce zero strategy returns."""
        close = pd.Series([100, 110, 121])
        positions = pd.Series([0.0, 0.0, 0.0])
        log_rets, _cumulative = calculate_log_returns(close, positions)
        # All strategy returns should be NaN (shift) or 0
        non_null = log_rets.dropna()
        assert (non_null == 0).all()

    def test_shift_applied(self):
        """Position signal is shifted by 1 (no look-ahead)."""
        close = pd.Series([100, 110, 105])
        positions = pd.Series([0.0, 1.0, 1.0])
        log_rets, _ = calculate_log_returns(close, positions)
        # Day 1: position_{t-1}=NaN → NaN strategy return
        # Day 2: position_{t-1}=0 → 0 strategy return
        # Day 3: position_{t-1}=1 → 1 * ln(105/110)
        assert pd.isna(log_rets.iloc[0])
        assert log_rets.iloc[1] == 0.0
        assert log_rets.iloc[2] == pytest.approx(np.log(105 / 110))

    def test_cumulative_compounding(self):
        """Cumulative should compound correctly."""
        close = pd.Series([100, 110, 121])
        positions = pd.Series([1.0, 1.0, 1.0])
        _, cumulative = calculate_log_returns(close, positions)
        # Final cumulative = exp(sum of log returns from day 2,3) - 1
        # = exp(ln(110/100) + ln(121/110)) - 1 = 121/100 - 1 = 0.21
        assert cumulative.iloc[-1] == pytest.approx(0.21)


# ---------------------------------------------------------------------------
# apply_friction
# ---------------------------------------------------------------------------


class TestApplyFriction:
    """Tests for apply_friction()."""

    def test_no_trades_no_friction(self):
        """No entry/exit signals = no friction deducted."""
        returns = pd.Series([0.01, -0.005, 0.02])
        entry = pd.Series([False, False, False])
        exit_sig = pd.Series([False, False, False])
        result, num_trades = apply_friction(returns, entry, exit_sig)
        pd.testing.assert_series_equal(result, returns)
        assert num_trades == 0

    def test_single_entry_trade(self):
        """One entry on day 1 should deduct friction on that day."""
        returns = pd.Series([0.01, 0.02, 0.01])
        entry = pd.Series([False, True, False])
        exit_sig = pd.Series([False, False, False])
        result, num_trades = apply_friction(returns, entry, exit_sig)
        total_friction = EXCHANGE_FEE * 2 + SLIPPAGE * 2
        assert result.iloc[1] == pytest.approx(0.02 - total_friction)
        assert num_trades == 1

    def test_entry_and_exit_same_day(self):
        """Entry + exit on same day = 1 trade (clipped)."""
        returns = pd.Series([0.01, 0.02])
        entry = pd.Series([False, True])
        exit_sig = pd.Series([False, True])
        result, num_trades = apply_friction(returns, entry, exit_sig)
        # Both entry and exit on day 1 → clip to 1 trade
        total_friction = EXCHANGE_FEE * 2 + SLIPPAGE * 2
        assert result.iloc[1] == pytest.approx(0.02 - total_friction)
        assert num_trades == 1

    def test_multiple_trades(self):
        """Multiple trade days should each get friction deducted."""
        returns = pd.Series([0.01, 0.02, -0.01, 0.03])
        entry = pd.Series([False, True, False, True])
        exit_sig = pd.Series([False, False, True, False])
        result, num_trades = apply_friction(returns, entry, exit_sig)
        total_friction = EXCHANGE_FEE * 2 + SLIPPAGE * 2
        assert result.iloc[1] == pytest.approx(0.02 - total_friction)
        assert result.iloc[2] == pytest.approx(-0.01 - total_friction)
        assert result.iloc[3] == pytest.approx(0.03 - total_friction)
        assert num_trades == 3

    def test_friction_constants(self):
        """Verify friction constants match documented rates."""
        assert EXCHANGE_FEE == 0.001  # 0.1%
        assert SLIPPAGE == 0.0005  # 0.05%
        # Round trip: entry fee + exit fee + entry slippage + exit slippage
        round_trip = EXCHANGE_FEE * 2 + SLIPPAGE * 2
        assert round_trip == pytest.approx(0.003)  # 0.3%

    def test_max_leverage_constant(self):
        """Max leverage should be 1.0 (no leverage)."""
        assert MAX_LEVERAGE == 1.0
