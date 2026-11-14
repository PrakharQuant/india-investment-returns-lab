"""
Fama-MacBeth Analysis Page
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from econometrics.fama_macbeth import fama_macbeth

st.set_page_config(page_title="Fama-MacBeth", layout="wide")

st.title("Fama-MacBeth Cross-Sectional Regressions")
st.markdown("Monthly cross-sectional regressions of returns on investment, profitability, size, and book-to-market.")

# Generate demo cross-sectional panel
np.random.seed(42)
n_months = 60
n_firms = 80
records = []
for t in range(n_months):
    for i in range(n_firms):
        inv = np.random.normal(0.12, 0.08)
        prof = np.random.normal(0.18, 0.06)
        size = np.random.normal(10, 1.2)
        bm = np.random.normal(0.7, 0.3)
        # Return with negative investment premium
        ret = 0.008 - 0.04 * inv + 0.06 * prof - 0.002 * size + 0.01 * bm + np.random.normal(0, 0.08)
        records.append({
            "date": t,
            "return": ret,
            "investment": inv,
            "profitability": prof,
            "size": size,
            "bm": bm,
        })

df = pd.DataFrame(records)

result = fama_macbeth(df, dependent="return", independents=["investment", "profitability", "size", "bm"])

st.subheader("Average Coefficients (Demonstration Mode – Synthetic Data)")

if "error" not in result:
    avg = result["average_coefficients"]
    se = result["standard_errors"]
    tstat = result["t_statistics"]
    
    results_df = pd.DataFrame({
        "Average Coefficient": avg,
        "Std. Error": se,
        "t-statistic": tstat,
    })
    st.dataframe(results_df.style.format("{:.4f}"), use_container_width=True)
    
    st.metric("Number of periods", result["n_periods"])
    
    # Coefficient plot
    fig = go.Figure(go.Bar(
        x=list(avg.keys()),
        y=list(avg.values()),
        marker_color=["#FF5252" if v < 0 else "#00C853" for v in avg.values()]
    ))
    fig.update_layout(title="Fama-MacBeth Average Coefficients (Demo)", template="plotly_dark", yaxis_title="Coefficient")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(result["error"])

st.info("These are results from synthetic demonstration data. In Research Mode the same Fama-MacBeth procedure runs on your uploaded fundamentals and prices with Newey-West standard errors.")
