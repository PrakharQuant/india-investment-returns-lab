"""
Portfolio Construction Page
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.title("Portfolio Construction")

st.markdown("### Investment Quintile Portfolios")

# Demo cumulative wealth
dates = pd.date_range("2016-01", "2025-12", freq="ME")
np.random.seed(42)
q1 = np.cumprod(1 + np.random.normal(0.01, 0.04, len(dates)))
q5 = np.cumprod(1 + np.random.normal(0.006, 0.05, len(dates)))
cma = q1 / q5

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=q1, name="Q1 Conservative", line=dict(color="#00C853")))
fig.add_trace(go.Scatter(x=dates, y=q5, name="Q5 Aggressive", line=dict(color="#FF5252")))
fig.add_trace(go.Scatter(x=dates, y=cma, name="CMA (Q1-Q5)", line=dict(color="#00D4AA", dash="dash")))
fig.update_layout(title="Cumulative Wealth of Investment Quintiles (Demo)", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.info("In Research Mode this chart is computed from actual data with proper look-ahead controls.")
