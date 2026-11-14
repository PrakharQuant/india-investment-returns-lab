"""
Configuration settings for India Investment Returns Lab (IIRL).
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
TEMPLATES_DIR = DATA_DIR / "templates"
SAMPLE_DIR = DATA_DIR / "sample"
PROCESSED_DIR = DATA_DIR / "processed"

DEFAULT_UNIVERSE = "Nifty 500"
FORMATION_MONTH = 6  # June formation
HOLDING_MONTHS = 12
REPORTING_LAG_MONTHS = 6
RANDOM_SEED = 42

INVESTMENT_MEASURES = {
    "investment_rate": "Capital Expenditure / Lagged Net Fixed Assets",
    "asset_growth": "(Total Assets_t - Total Assets_t-1) / Total Assets_t-1",
    "net_investment_rate": "(Capital Expenditure - Depreciation) / Lagged Net Fixed Assets",
}

PROFITABILITY_MEASURES = {
    "operating_profitability": "Operating Profit / Book Equity",
    "roa": "Operating Profit / Lagged Total Assets",
}

COLORS = {
    "navy": "#0A1929",
    "charcoal": "#1A2332",
    "accent": "#00D4AA",
    "positive": "#00C853",
    "negative": "#FF5252",
    "neutral": "#B0BEC5",
}
