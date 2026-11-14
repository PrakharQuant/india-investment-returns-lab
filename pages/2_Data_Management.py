"""
Data Management Page
"""
import streamlit as st
import pandas as pd
from io import StringIO

st.title("Data Management")

st.markdown("""
### Upload Financial Data
Upload annual financial statements in CSV or XLSX format.  
Download the template below for the required schema.
""")

# Template download
template = pd.DataFrame({
    "ticker": ["RELIANCE.NS"],
    "company_name": ["Reliance Industries"],
    "fiscal_year": [2024],
    "fiscal_year_end": ["2024-03-31"],
    "announcement_date": ["2024-05-15"],
    "total_assets": [1000000000000],
    "net_fixed_assets": [400000000000],
    "capital_expenditure": [50000000000],
    "depreciation": [30000000000],
    "operating_profit": [120000000000],
    "net_income": [80000000000],
    "book_equity": [500000000000],
    "market_cap": [1500000000000],
    "industry": ["Energy"],
    "sector": ["Oil & Gas"],
})
st.download_button(
    "Download Financial Data Template (CSV)",
    template.to_csv(index=False),
    "financial_data_template.csv",
    "text/csv",
)

uploaded = st.file_uploader("Upload Fundamentals CSV/XLSX", type=["csv", "xlsx"])
if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
    st.success(f"Loaded {len(df)} records")
    st.dataframe(df.head())
    st.session_state.fundamentals = df

st.markdown("### Synthetic Demonstration Data")
if st.button("Load Synthetic Dataset"):
    from src.data.synthetic_generator import generate_synthetic_fundamentals
    df = generate_synthetic_fundamentals()
    st.session_state.fundamentals = df
    st.success("Synthetic dataset loaded (clearly labelled as DEMO).")
