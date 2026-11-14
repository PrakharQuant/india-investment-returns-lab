"""
Research Overview Page
"""
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Research Overview", layout="wide")

st.title("Research Overview")
st.markdown("""
### Central Hypothesis
Indian companies with **conservative investment policies** generate higher subsequent stock returns than companies with aggressive investment policies, after controlling for size, value, profitability and market risk.

**Secondary Hypotheses:**
- H1: Investment intensity negatively predicts subsequent stock returns.
- H2: More profitable companies generate higher subsequent stock returns.
- H3: The investment-return relationship remains significant after controlling for conventional factors.
- H4: The relationship varies across market regimes.
- H5: Investment and profitability jointly explain cross-sectional return differences.

*All results are empirical associations, not causal claims.*
""")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Companies", "100 (Demo)")
with col2:
    st.metric("Sample Period", "2015–2025")
with col3:
    st.metric("Investment Spread (Demo)", "+4.2% ann.")
with col4:
    st.metric("t-statistic (Demo)", "2.1")

st.warning("Currently running in Demonstration Mode with synthetic data. Upload real fundamentals in Data Management for research analysis.")

st.markdown("""
### Data Quality Warnings
- Synthetic observations are clearly labelled and must never be mixed with real market data.
- Yahoo Finance does not provide complete historical Indian fundamentals.
- Using only current index constituents introduces survivorship bias.
""")
