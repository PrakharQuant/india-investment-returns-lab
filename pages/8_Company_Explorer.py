"""
Company Explorer Page
"""
import streamlit as st

st.title("Company Explorer")
st.markdown("Search and inspect individual company investment history, profitability, and quintile classification.")

ticker = st.text_input("Ticker (e.g. SYN001.NS)", "SYN001.NS")
if st.button("Explore"):
    st.info(f"Displaying synthetic history for {ticker} in Demonstration Mode.")
    st.line_chart({"Investment Rate": [0.12, 0.15, 0.10, 0.08, 0.11]})
