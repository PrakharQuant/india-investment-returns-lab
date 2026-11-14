"""
Profitability and other characteristic construction.
"""
import pandas as pd
import numpy as np

def calculate_operating_profitability(df: pd.DataFrame) -> pd.DataFrame:
    """Operating Profitability = Operating Profit / Book Equity."""
    df["operating_profitability"] = df["operating_profit"] / df["book_equity"]
    df["operating_profitability"] = df["operating_profitability"].replace([np.inf, -np.inf], np.nan)
    return df

def calculate_roa(df: pd.DataFrame) -> pd.DataFrame:
    """ROA = Operating Profit / Lagged Total Assets."""
    df = df.sort_values(["ticker", "fiscal_year"])
    df["lagged_total_assets"] = df.groupby("ticker")["total_assets"].shift(1)
    df["roa"] = df["operating_profit"] / df["lagged_total_assets"]
    df["roa"] = df["roa"].replace([np.inf, -np.inf], np.nan)
    return df

def calculate_book_to_market(df: pd.DataFrame) -> pd.DataFrame:
    """Book-to-Market = Book Equity / Market Cap."""
    df["book_to_market"] = df["book_equity"] / df["market_cap"]
    df["book_to_market"] = df["book_to_market"].replace([np.inf, -np.inf], np.nan)
    return df

def calculate_size(df: pd.DataFrame) -> pd.DataFrame:
    """Size = log(Market Cap)."""
    df["size"] = np.log(df["market_cap"].clip(lower=1))
    return df
