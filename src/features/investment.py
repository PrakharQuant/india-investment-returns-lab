"""
Investment intensity variable construction.
"""
import pandas as pd
import numpy as np

def calculate_investment_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Investment Rate = Capex / Lagged Net Fixed Assets (I/K)."""
    df = df.sort_values(["ticker", "fiscal_year"])
    df["lagged_net_fixed_assets"] = df.groupby("ticker")["net_fixed_assets"].shift(1)
    df["investment_rate"] = df["capital_expenditure"] / df["lagged_net_fixed_assets"]
    df["investment_rate"] = df["investment_rate"].replace([np.inf, -np.inf], np.nan)
    return df

def calculate_asset_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Asset Growth = (Assets_t - Assets_t-1) / Assets_t-1."""
    df = df.sort_values(["ticker", "fiscal_year"])
    df["lagged_total_assets"] = df.groupby("ticker")["total_assets"].shift(1)
    df["asset_growth"] = (df["total_assets"] - df["lagged_total_assets"]) / df["lagged_total_assets"]
    df["asset_growth"] = df["asset_growth"].replace([np.inf, -np.inf], np.nan)
    return df

def calculate_net_investment_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Net Investment Rate = (Capex - Dep) / Lagged Net Fixed Assets."""
    df = df.sort_values(["ticker", "fiscal_year"])
    df["lagged_net_fixed_assets"] = df.groupby("ticker")["net_fixed_assets"].shift(1)
    df["net_investment_rate"] = (df["capital_expenditure"] - df["depreciation"]) / df["lagged_net_fixed_assets"]
    df["net_investment_rate"] = df["net_investment_rate"].replace([np.inf, -np.inf], np.nan)
    return df

def winsorize(series: pd.Series, lower=0.01, upper=0.99) -> pd.Series:
    """Winsorize extreme values."""
    return series.clip(lower=series.quantile(lower), upper=series.quantile(upper))
