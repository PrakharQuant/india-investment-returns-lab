"""
Performance metrics.
"""
import pandas as pd
import numpy as np

def calculate_performance(returns: pd.Series) -> dict:
    """Calculate standard performance metrics."""
    if len(returns) == 0:
        return {}
    ann_return = (1 + returns.mean()) ** 12 - 1
    vol = returns.std() * np.sqrt(12)
    sharpe = ann_return / vol if vol > 0 else np.nan
    cum = (1 + returns).cumprod()
    peak = cum.cummax()
    drawdown = (cum - peak) / peak
    max_dd = drawdown.min()
    return {
        "annualized_return": ann_return,
        "volatility": vol,
        "sharpe_ratio": sharpe,
        "max_drawdown": max_dd,
        "cumulative_wealth": cum.iloc[-1] if len(cum) > 0 else 1.0,
    }
