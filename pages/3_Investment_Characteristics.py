"""
Investment Characteristics Page
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from features.investment import calculate_investment_rate, calculate_asset_growth
from features.profitability import calculate_operating_profitability, calculate_size, calculate_book_to_market

st.set_page_config(page_title="Investment Characteristics", layout="wide")

st.title("Investment Characteristics")
st.markdown("Interactive analysis of investment intensity, profitability, and their relationship with subsequent returns.")

# Load data from session or generate demo
if "fundamentals" in st.session_state and st.session_state.fundamentals is not None:
    df = st.session_state.fundamentals.copy()
    st.success(f"Using loaded data: {len(df)} observations")
else:
    st.warning("No data loaded. Showing synthetic demonstration data.")
    from data.synthetic_generator import generate_synthetic_fundamentals
    df = generate_synthetic_fundamentals(n_companies=50, n_years=8)

# Compute characteristics
df = calculate_investment_rate(df)
df = calculate_asset_growth(df)
df = calculate_operating_profitability(df)
df = calculate_size(df)
df = calculate_book_to_market(df)

# Clean for display
df_clean = df.dropna(subset=["investment_rate", "operating_profitability"]).copy()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Investment Rate Distribution")
    fig = px.histogram(df_clean, x="investment_rate", nbins=30, title="Investment Rate (I/K)",
                       color_discrete_sequence=["#00D4AA"])
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Investment vs Profitability")
    fig = px.scatter(df_clean, x="investment_rate", y="operating_profitability",
                     hover_data=["ticker", "fiscal_year"], title="Investment Rate vs Operating Profitability",
                     color_discrete_sequence=["#00D4AA"])
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Summary Statistics")
st.dataframe(df_clean[["investment_rate", "asset_growth", "operating_profitability", "size", "book_to_market"]].describe().style.format("{:.3f}"), use_container_width=True)

st.subheader("Industry-level Average Investment Rate")
if "industry" in df_clean.columns:
    industry_avg = df_clean.groupby("industry")["investment_rate"].mean().reset_index()
    fig = px.bar(industry_avg, x="industry", y="investment_rate", title="Average Investment Rate by Industry",
                 color_discrete_sequence=["#00D4AA"])
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.info("All charts use the currently loaded dataset (synthetic demo or your uploaded fundamentals). Subsequent returns analysis appears in Portfolio Construction.")
