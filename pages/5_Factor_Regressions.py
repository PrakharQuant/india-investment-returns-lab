"""
Factor Regressions Page
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from econometrics.factor_models import run_factor_regression

st.set_page_config(page_title="Factor Regressions", layout="wide")

st.title("Factor Regressions")
st.markdown("Time-series regressions of portfolio excess returns on market and multi-factor models.")

# Generate demo data
np.random.seed(42)
n = 120  # months
dates = pd.date_range("2015-01", periods=n, freq="ME")
mkt = np.random.normal(0.008, 0.05, n)
smb = np.random.normal(0.002, 0.03, n)
hml = np.random.normal(0.001, 0.03, n)
rmw = np.random.normal(0.003, 0.025, n)
cma = np.random.normal(-0.001, 0.02, n)

# CMA portfolio excess returns (demo)
cma_port = 0.004 + 0.15 * mkt - 0.3 * cma + np.random.normal(0, 0.02, n)

factors = pd.DataFrame({"MKT": mkt, "SMB": smb, "HML": hml, "RMW": rmw, "CMA": cma}, index=dates)
port_ret = pd.Series(cma_port, index=dates)

# Run regressions
model1 = run_factor_regression(port_ret, factors[["MKT"]])
model2 = run_factor_regression(port_ret, factors[["MKT", "SMB", "HML"]])
model3 = run_factor_regression(port_ret, factors)

st.subheader("Regression Results (Demonstration Mode – Synthetic Data)")

cols = st.columns(3)
with cols[0]:
    st.markdown("**Model 1: Market**")
    st.metric("Alpha (monthly)", f"{model1['alpha']:.4f}")
    st.metric("Alpha t-stat", f"{model1['alpha_tstat']:.2f}")
    st.metric("R²", f"{model1['rsquared']:.3f}")

with cols[1]:
    st.markdown("**Model 2: FF3**")
    st.metric("Alpha (monthly)", f"{model2['alpha']:.4f}")
    st.metric("Alpha t-stat", f"{model2['alpha_tstat']:.2f}")
    st.metric("R²", f"{model2['rsquared']:.3f}")

with cols[2]:
    st.markdown("**Model 3: FF5-style**")
    st.metric("Alpha (monthly)", f"{model3['alpha']:.4f}")
    st.metric("Alpha t-stat", f"{model3['alpha_tstat']:.2f}")
    st.metric("R²", f"{model3['rsquared']:.3f}")

# Coefficient plot for Model 3
params = model3["params"]
tstats = model3["tstats"]
coef_df = pd.DataFrame({
    "Coefficient": list(params.values()),
    "t-stat": list(tstats.values())
}, index=params.keys())

st.subheader("Factor Loadings (Model 3)")
st.dataframe(coef_df.style.format("{:.4f}"), use_container_width=True)

fig = go.Figure(go.Bar(
    x=list(params.keys()),
    y=list(params.values()),
    marker_color="#00D4AA"
))
fig.update_layout(title="Factor Coefficients (Demo)", template="plotly_dark", yaxis_title="Coefficient")
st.plotly_chart(fig, use_container_width=True)

st.info("These are results from synthetic demonstration data. In Research Mode the same functions run on your uploaded data with proper look-ahead controls.")
