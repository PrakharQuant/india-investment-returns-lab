"""
Robustness Tests Page
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Robustness Tests", layout="wide")

st.title("Robustness Tests")
st.markdown("Sensitivity analysis across alternative measures, weighting schemes, formation periods, industry neutrality, winsorisation, and market regimes.")

st.subheader("Sensitivity Dashboard (Demonstration Mode)")

# Demo sensitivity results
sensitivity = pd.DataFrame({
    "Specification": [
        "Baseline (I/K, EW, June formation)",
        "Asset Growth instead of I/K",
        "Value-weighted instead of Equal-weighted",
        "December formation",
        "Industry-neutral sorts",
        "Winsorised at 1%/99%",
        "Exclude financials",
        "Bull market subsample",
        "Bear market subsample",
        "Minimum market-cap filter",
    ],
    "CMA Annualised Spread": [4.2, 3.8, 3.5, 4.0, 3.9, 4.3, 4.5, 5.1, 2.8, 4.1],
    "t-statistic": [2.1, 1.9, 1.7, 2.0, 1.8, 2.2, 2.3, 2.4, 1.3, 2.0],
})

st.dataframe(sensitivity.style.format({"CMA Annualised Spread": "{:.1f}%", "t-statistic": "{:.2f}"}), use_container_width=True)

fig = go.Figure()
fig.add_trace(go.Bar(
    x=sensitivity["Specification"],
    y=sensitivity["CMA Annualised Spread"],
    marker_color="#00D4AA",
    name="Annualised Spread (%)"
))
fig.update_layout(
    title="CMA Spread Across Robustness Specifications (Demo)",
    template="plotly_dark",
    xaxis_tickangle=-45,
    yaxis_title="Annualised Return Spread (%)"
)
st.plotly_chart(fig, use_container_width=True)

st.info("""
These figures illustrate the structure of the robustness dashboard.  
In Research Mode the same tests are recomputed from your uploaded data with proper look-ahead bias controls, alternative investment measures, equal- vs value-weighting, different formation months, industry neutrality, winsorisation, exclusion of financials, and regime splits.
""")

st.markdown("""
### Available Robustness Checks
1. Alternative investment measures (I/K, Asset Growth, Net Investment)
2. Equal-weighted vs value-weighted portfolios
3. Alternative portfolio formation periods
4. Industry-neutral portfolio sorts
5. Winsorisation of extreme accounting ratios
6. Exclusion of financial companies
7. Bull-market vs bear-market analysis
8. Alternative holding periods
9. Minimum market-capitalisation filters
10. Subsample stability
""")
