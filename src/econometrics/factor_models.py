"""
Time-series factor regressions.
"""
import pandas as pd
import statsmodels.api as sm
import numpy as np

def run_factor_regression(portfolio_returns: pd.Series, factors: pd.DataFrame, rf: pd.Series = None) -> dict:
    """Run market model or multi-factor regression with Newey-West standard errors."""
    if rf is not None:
        excess = portfolio_returns - rf
    else:
        excess = portfolio_returns
    
    X = sm.add_constant(factors)
    model = sm.OLS(excess, X, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 6})
    
    return {
        "alpha": model.params.get("const", np.nan),
        "alpha_tstat": model.tvalues.get("const", np.nan),
        "alpha_pvalue": model.pvalues.get("const", np.nan),
        "params": model.params.to_dict(),
        "tstats": model.tvalues.to_dict(),
        "rsquared": model.rsquared,
        "adj_rsquared": model.rsquared_adj,
        "nobs": model.nobs,
    }
