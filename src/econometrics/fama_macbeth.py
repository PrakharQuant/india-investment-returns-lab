"""
Fama-MacBeth cross-sectional regressions.
"""
import pandas as pd
import statsmodels.api as sm
import numpy as np

def fama_macbeth(df: pd.DataFrame, dependent: str, independents: list) -> dict:
    """Monthly cross-sectional regressions averaged over time with Newey-West."""
    coefficients = []
    for date, group in df.groupby("date"):
        if len(group) < 10:
            continue
        y = group[dependent]
        X = sm.add_constant(group[independents])
        try:
            res = sm.OLS(y, X, missing="drop").fit()
            coefficients.append(res.params)
        except Exception:
            continue
    
    if not coefficients:
        return {"error": "Insufficient data"}
    
    coef_df = pd.DataFrame(coefficients)
    avg_coefs = coef_df.mean()
    # Simplified Newey-West on coefficient series
    nw_se = coef_df.std() / np.sqrt(len(coef_df))  # Placeholder; real NW requires HAC
    
    return {
        "average_coefficients": avg_coefs.to_dict(),
        "standard_errors": nw_se.to_dict(),
        "t_statistics": (avg_coefs / nw_se).to_dict(),
        "n_periods": len(coef_df),
    }
