# India Investment Returns Lab (IIRL)

**A Production-Based Asset Pricing Research Platform for the Indian Equity Market**

![IIRL Banner](https://via.placeholder.com/800x200/0A1929/00D4AA?text=India+Investment+Returns+Lab)

## Overview

The **India Investment Returns Lab (IIRL)** is a professional quantitative research platform designed to investigate the relationship between corporate investment intensity, profitability, firm characteristics, and subsequent stock returns in the Indian equity market.

Inspired by production-based asset pricing theory (Tobin's q, adjustment costs) and the Fama-French investment and profitability factors, IIRL provides a reproducible laboratory for empirical asset pricing research. It is **not** a generic stock screener.

### Central Hypothesis

> Indian companies with conservative investment policies generate higher subsequent stock returns than companies with aggressive investment policies, after controlling for size, value, profitability and market risk.

**Important**: All analyses report empirical associations. The platform does **not** claim causal relationships.

## Features

- Modular data ingestion (Yahoo Finance prices + user-uploaded fundamentals)
- Look-ahead bias controls (announcement-date or conservative reporting lag)
- Investment intensity, profitability, size, and value characteristic construction
- Quintile portfolio sorts (equal- and value-weighted)
- Conservative-Minus-Aggressive (CMA) long-short portfolio
- Time-series factor regressions (Market, FF3, FF5-style)
- Fama-MacBeth cross-sectional regressions
- Optional panel regressions with fixed effects
- Comprehensive robustness tests and sensitivity dashboard
- Interactive Streamlit dashboard with professional quantitative finance aesthetic
- Synthetic demonstration dataset (clearly labelled)
- Automated tests and reproducibility focus

## Theoretical Foundations

- Tobin (1969): Tobin's q and investment theory
- Hayashi (1982): Marginal q and average q
- Cochrane (1991): Production-based asset pricing
- Liu, Whited & Zhang (2009): Investment-based expected returns
- Fama & French (2015): Five-factor model (including investment and profitability)

## Quick Start

```bash
git clone https://github.com/PrakharQuant/india-investment-returns-lab.git
cd india-investment-returns-lab
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

The application starts in **Demonstration Mode** with synthetic data. Switch to Research Mode to upload real financial data.

## Data Requirements

- Daily adjusted stock prices (via yfinance or upload)
- Annual financial statements (user upload — Yahoo Finance fundamentals are incomplete for Indian firms)
- Optional: historical index constituents, risk-free rate, factor data

Downloadable CSV templates are provided in the Data Management section.

## Deployment (Render)

See `render.yaml` and the Deployment section below.

## Author & Credits

**Built by Prakhar Gupta**

- LinkedIn: [Prakhar Gupta](https://www.linkedin.com/in/prakhar-gupta)
- X (Twitter): [@PrakharQuant](https://x.com/PrakharQuant)
- Email: [bestofprakhar@gmail.com](mailto:bestofprakhar@gmail.com)
- Website: [prakharquant.github.io](https://prakharquant.github.io/)

## License

MIT License — Open source for research and educational use.

## Known Limitations

- Yahoo Finance does not provide complete historical Indian company fundamentals.
- Analysis using only current index constituents is subject to survivorship bias (explicitly labelled).
- Synthetic data is for demonstration only and must never be mixed with real data.
- Results are empirical associations, not causal claims.

---

**Prioritising statistical correctness and research transparency.**
