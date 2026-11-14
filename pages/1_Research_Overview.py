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
### Theoretical Foundations
This laboratory is grounded in production-based asset pricing.

- **Tobin (1969)**: Firms invest when the market value of capital exceeds its replacement cost (Tobin’s q > 1).
- **Hayashi (1982)**: Under certain conditions marginal q equals average q, linking investment to market valuations.
- **Cochrane (1991)**: Production-based asset pricing — high investment today implies low expected returns (adjustment costs).
- **Liu, Whited & Zhang (2009)**: Investment-based models of expected stock returns.
- **Fama & French (2015)**: The five-factor model explicitly includes investment (CMA) and profitability (RMW) factors.

**Key intuition**: Companies that invest aggressively today have lower expected future returns because the high investment already capitalises expected cash-flow growth. Conservative investors (low I/K) are associated with higher subsequent stock returns.

The empirical tests in this lab examine whether this relationship holds in the Indian equity market after standard risk and characteristic controls.
""")

st.markdown("""
### Data Quality Warnings
- Synthetic observations are clearly labelled and must never be mixed with real market data.
- Yahoo Finance does not provide complete historical Indian fundamentals.
- Using only current index constituents introduces survivorship bias.
""")
