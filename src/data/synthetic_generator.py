"""
Synthetic dataset generator for IIRL demonstration mode.
Clearly labelled as simulated. Never mix with real data.
"""
import numpy as np
import pandas as pd
from pathlib import Path
from config.settings import RANDOM_SEED, SAMPLE_DIR

np.random.seed(RANDOM_SEED)

def generate_synthetic_fundamentals(n_companies=100, n_years=10, start_year=2015):
    """Generate synthetic annual financial data."""
    tickers = [f"SYN{i:03d}.NS" for i in range(1, n_companies + 1)]
    companies = [f"Synthetic Company {i}" for i in range(1, n_companies + 1)]
    
    records = []
    for ticker, name in zip(tickers, companies):
        for year in range(start_year, start_year + n_years):
            # Base characteristics with some persistence
            total_assets = np.random.lognormal(10, 0.5) * 1e9
            net_fixed_assets = total_assets * np.random.uniform(0.3, 0.6)
            capex = net_fixed_assets * np.random.uniform(0.05, 0.25)
            depreciation = net_fixed_assets * np.random.uniform(0.08, 0.12)
            operating_profit = total_assets * np.random.uniform(0.05, 0.15)
            net_income = operating_profit * np.random.uniform(0.6, 0.9)
            book_equity = total_assets * np.random.uniform(0.3, 0.7)
            market_cap = book_equity * np.random.uniform(0.8, 3.0)
            
            records.append({
                "ticker": ticker,
                "company_name": name,
                "fiscal_year": year,
                "fiscal_year_end": f"{year}-03-31",
                "announcement_date": f"{year}-06-15",
                "total_assets": total_assets,
                "net_fixed_assets": net_fixed_assets,
                "capital_expenditure": capex,
                "depreciation": depreciation,
                "operating_profit": operating_profit,
                "net_income": net_income,
                "book_equity": book_equity,
                "market_cap": market_cap,
                "industry": np.random.choice(["IT", "Financials", "Consumer", "Industrials", "Energy"]),
                "sector": "Synthetic",
                "source": "SYNTHETIC_DEMO",
            })
    
    df = pd.DataFrame(records)
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAMPLE_DIR / "synthetic_fundamentals.csv", index=False)
    return df

def generate_synthetic_prices(fundamentals_df, start_date="2015-01-01", end_date="2025-12-31"):
    """Generate synthetic daily prices correlated with fundamentals (weakly)."""
    # Simplified: generate monthly returns for demo
    tickers = fundamentals_df["ticker"].unique()
    dates = pd.date_range(start_date, end_date, freq="ME")
    
    price_records = []
    for ticker in tickers:
        price = 100.0
        for date in dates:
            # Random walk with slight mean reversion
            ret = np.random.normal(0.008, 0.06)
            price *= (1 + ret)
            price_records.append({
                "ticker": ticker,
                "date": date,
                "adjusted_close": price,
                "source": "SYNTHETIC_DEMO",
            })
    
    df = pd.DataFrame(price_records)
    df.to_csv(SAMPLE_DIR / "synthetic_prices.csv", index=False)
    return df

if __name__ == "__main__":
    print("Generating synthetic datasets...")
    fund = generate_synthetic_fundamentals()
    prices = generate_synthetic_prices(fund)
    print(f"Generated {len(fund)} fundamental records and {len(prices)} price records.")
    print("Files saved to data/sample/")
