"""
Portfolio sorting and construction.
"""
import pandas as pd
import numpy as np

def assign_quintiles(df: pd.DataFrame, characteristic: str, n_quantiles=5) -> pd.DataFrame:
    """Assign companies to quintiles based on a characteristic (Q1 = lowest)."""
    df = df.copy()
    df["quintile"] = df.groupby("formation_date")[characteristic].transform(
        lambda x: pd.qcut(x.rank(method="first"), n_quantiles, labels=False, duplicates="drop") + 1
    )
    return df

def calculate_portfolio_returns(
    prices: pd.DataFrame,
    portfolios: pd.DataFrame,
    weighting: str = "equal",
) -> pd.DataFrame:
    """Calculate equal- or value-weighted portfolio returns."""
    # Simplified implementation for demo
    merged = prices.merge(portfolios[["ticker", "formation_date", "quintile", "market_cap"]], on="ticker", how="inner")
    # Aggregate by date and quintile
    if weighting == "equal":
        returns = merged.groupby(["date", "quintile"])["ret"].mean().unstack()
    else:
        merged["weight"] = merged.groupby(["date", "quintile"])["market_cap"].transform(lambda x: x / x.sum())
        returns = merged.groupby(["date", "quintile"]).apply(lambda g: (g["ret"] * g["weight"]).sum()).unstack()
    returns.columns = [f"Q{int(c)}" for c in returns.columns]
    returns["CMA"] = returns["Q1"] - returns["Q5"]
    return returns
