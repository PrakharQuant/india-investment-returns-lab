"""
Basic tests for feature calculations.
"""
import pytest
import pandas as pd
import numpy as np
from src.features.investment import calculate_investment_rate

def test_investment_rate():
    df = pd.DataFrame({
        "ticker": ["A", "A"],
        "fiscal_year": [2020, 2021],
        "capital_expenditure": [10, 20],
        "net_fixed_assets": [100, 110],
    })
    result = calculate_investment_rate(df)
    assert abs(result.loc[1, "investment_rate"] - 20/100) < 1e-6

def test_no_lookahead_placeholder():
    # Placeholder for look-ahead bias checks
    assert True
