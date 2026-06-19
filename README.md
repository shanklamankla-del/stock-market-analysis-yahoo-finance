# Tech Stock Growth and Risk Analysis

## Project Overview

This project analyzes major technology and semiconductor stocks using historical stock data from Yahoo Finance. The goal is to compare stock growth, volatility, and risk-adjusted performance over time.

The project started as a Python-based stock analysis project and was expanded into a reporting/dashboard project using Power BI.

Instead of only showing stock price movement, this project attempts to answer:

* Which stocks had the strongest growth?
* Which stocks had the highest volatility?
* Which stocks had the best return compared to risk?
* How do semiconductor-related stocks compare to broader technology companies?
* How can this data be presented in a way that is useful for a non-technical stakeholder?

## Business Question

How did major technology and semiconductor stocks perform over the analysis period, and which stocks provided the strongest growth relative to their volatility?

## Stocks Analyzed

The project focuses on major technology and semiconductor-related stocks:

* `NVDA` — Nvidia
* `AMD` — Advanced Micro Devices
* `MU` — Micron Technology
* `AAPL` — Apple
* `MSFT` — Microsoft
* `AMZN` — Amazon
* `^GSPC` — S&P 500 benchmark

## Tools Used

* Python
* pandas
* yfinance
* matplotlib
* Power BI
* Git/GitHub

## Project Structure

```text
stock-market-analysis-yahoo-finance/
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── stock_prices.csv
│   │
│   └── processed/
│       ├── .gitkeep
│       ├── monthly_seasonality.csv
│       ├── powerbi_dashboard_data.csv
│       ├── powerbi_stock_prices.csv
│       ├── powerbi_stock_summary.csv
│       ├── quarterly_returns.csv
│       ├── total_returns.csv
│       └── volatility.csv
│
├── images/
│   └── charts/
│       ├── .gitkeep
│       ├── monthly_seasonality.png
│       ├── quarterly_returns.png
│       ├── stock_prices_over_time.png
│       ├── total_returns.png
│       └── volatility.png
│
├── notebooks/
│
├── powerbi/
│   └── stock_market_dashboard.pbix
│
├── src/
│   ├── analyze_returns.py
│   ├── download_data.py
│   ├── export_powerbi_data.py
│   ├── quarterly_analysis.py
│   ├── seasonality.py
│   └── visualize.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## How to Run This Project

### 1. Install required packages

Install the dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 2. Download stock data

Run the data download script.

```bash
python src/download_data.py
```

This downloads historical stock data from Yahoo Finance and saves it to:

```text
data/raw/stock_prices.csv
```

### 3. Analyze returns and volatility

Run the analysis script.

```bash
python src/analyze_returns.py
```

This calculates:

* Total return
* Daily returns
* Annualized volatility

The output files are saved in:

```text
data/processed/
```

### 4. Create Python charts

Run the visualization script.

```bash
python src/visualize.py
```

This creates charts and saves them to:

```text
images/charts/
```

### 5. Export Power BI dashboard data

Run the Power BI export script.

```bash
python src/export_powerbi_data.py
```

This creates a Power BI-friendly dataset:

```text
data/processed/powerbi_dashboard_data.csv
```

This file is used to build the Power BI dashboard.

## Python Analysis

The Python part of the project handles data collection, cleaning, and analysis.

The project calculates:

* Closing price trends
* Daily returns
* Total return percentage
* Annualized volatility
* Return-to-risk comparison

## Power BI Dashboard

This project includes a Power BI dashboard that uses the processed Yahoo Finance data.

The dashboard includes:

* A ticker slicer/dropdown
* A stock price trend line chart
* A total return card
* An annualized volatility card
* A risk vs return scatterplot
* A written insight explaining the results

The dashboard is designed to make the analysis easier to understand for a non-technical user or stakeholder.

## Dashboard Purpose

The Power BI dashboard helps answer:

* Which stock had the highest return?
* Which stock had the highest volatility?
* How much risk came with each stock’s return?
* How did individual stocks trend over time?
* How did Nvidia compare to other technology and semiconductor stocks?

## Key Insights

* Nvidia showed the strongest total return during the period analyzed.
* Nvidia also had high volatility, meaning the stock had larger price swings.
* Semiconductor-related companies such as Nvidia, AMD, and Micron showed different risk and return behavior compared to larger diversified technology companies.
* The S&P 500 benchmark helps compare individual stock performance against the broader market.
* The risk vs return scatterplot provides more insight than a simple stock price chart because it compares both growth and volatility.

## Example Dashboard Insight

NVDA showed the strongest total return during the period analyzed, but it also had higher volatility. This suggests that the stock had strong growth potential but also larger price swings compared to more stable companies.

## What I Learned

* How to download stock data using `yfinance`
* How to clean and analyze financial time series data with pandas
* How to calculate total return and daily returns
* How to calculate annualized volatility
* How to create charts using matplotlib
* How to prepare processed CSV files for dashboard tools
* How to build a basic Power BI dashboard
* How to communicate data insights to a non-technical audience
* How to improve a project based on feedback

## Future Improvements

* Add monthly seasonality analysis
* Add quarterly return analysis
* Add quarterly earnings data
* Add market event annotations
* Add memory/RAM/DRAM price event analysis
* Improve the Power BI dashboard layout
* Add more written business insights
* Compare semiconductor stocks against broader technology sector ETFs
* Deploy or publish the dashboard if possible

## Report

A full written analysis of the findings is available here:

[Stock Analysis Report](reports/stock_analysis_report.md)

## Disclaimer

This project is for educational and portfolio purposes only. It is not financial advice. The analysis is based on historical data and does not predict future stock performance.
