"""
India Investment Returns Lab (IIRL)
Main Streamlit Application Entry Point
"""
import streamlit as st
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config.settings import COLORS

st.set_page_config(
    page_title="India Investment Returns Lab (IIRL)",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for professional quantitative finance aesthetic and readable sidebar
st.markdown(f"""
<style>
    .stApp {{
        background-color: {COLORS['navy']};
        color: #E0E0E0;
    }}
    .stSidebar {{
        background-color: {COLORS['charcoal']} !important;
    }}
    .stSidebar .stMarkdown, .stSidebar p, .stSidebar label, .stSidebar .stRadio label,
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar span, .stSidebar div {{
        color: #E0E0E0 !important;
    }}
    .stSidebar .stRadio > div {{
        color: #E0E0E0 !important;
    }}
    [data-testid="stSidebar"] {{
        background-color: {COLORS['charcoal']};
    }}
    [data-testid="stSidebar"] * {{
        color: #E0E0E0 !important;
    }}
    h1, h2, h3 {{
        color: {COLORS['accent']};
    }}
    .metric-card {{
        background-color: {COLORS['charcoal']};
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid {COLORS['accent']};
    }}
</style>
""", unsafe_allow_html=True)

st.title("📈 India Investment Returns Lab (IIRL)")
st.markdown("""
**Production-Based Asset Pricing Research Platform**  
Investigating the investment–return relationship in Indian equities.

*Built by [Prakhar Gupta](https://github.com/PrakharQuant)*  
[LinkedIn](https://www.linkedin.com/in/prakhar-gupta) · [X](https://x.com/PrakharQuant) · [Email](mailto:bestofprakhar@gmail.com)
""")

st.info("Navigate using the sidebar. Start in **Demonstration Mode** with synthetic data, or switch to Research Mode to upload actual data.")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.markdown("""
    1. Research Overview  
    2. Data Management  
    3. Investment Characteristics  
    4. Portfolio Construction  
    5. Factor Regressions  
    6. Fama-MacBeth Analysis  
    7. Robustness Tests  
    8. Company Explorer  
    9. Research Report
    """)
    st.divider()
    mode = st.radio("Mode", ["Demonstration", "Research"])
    st.session_state.mode = mode
    if mode == "Demonstration":
        st.warning("All data is **synthetic**. For research use only.")

st.success("Application ready. Select a page from the sidebar to begin analysis.")
