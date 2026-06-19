# Stock Analysis Report

## 1. Introduction

This report analyzes the growth, volatility, and risk-adjusted performance of major technology and semiconductor-related stocks using historical stock data from Yahoo Finance.

The goal of this project was to move beyond a basic stock price chart and create a more useful reporting output for a stakeholder. Instead of only showing whether a stock increased or decreased, this analysis compares total return, volatility, and risk versus return across several companies.

## 2. Business Question

The main question this project tries to answer is:

**Which major technology or semiconductor-related stocks showed the strongest growth, and how much volatility came with that growth?**

This helps compare stocks not only by how much they grew, but also by how risky or unstable their price movement was during the analysis period.

## 3. Data Used

The data was collected using Python and the `yfinance` library. The project uses historical stock price data from Yahoo Finance.

The stocks analyzed were:

* NVDA — Nvidia
* AMD — Advanced Micro Devices
* MU — Micron Technology
* AAPL — Apple
* MSFT — Microsoft
* AMZN — Amazon
* ^GSPC — S&P 500 benchmark

The S&P 500 was included as a benchmark to compare individual stock performance against the broader market.

## 4. Methods

The project used Python to download, clean, analyze, and export stock data.

The main metrics calculated were:

* **Closing price trend:** Shows how stock prices changed over time.
* **Total return:** Measures how much each stock increased or decreased over the full analysis period.
* **Daily return:** Measures the percentage change from one trading day to the next.
* **Annualized volatility:** Measures how much the stock price moved up and down over time.
* **Risk vs return:** Compares total return against volatility to show whether higher returns came with higher risk.

The processed data was then used to create charts and a Power BI dashboard.

## 5. Key Findings

Nvidia had the strongest total return during the period analyzed. Its stock price increased much more than the other companies in the dataset.

However, Nvidia also showed higher volatility. This means that while Nvidia had strong growth, it also had larger price swings compared to more stable companies.

The risk vs return scatterplot showed that semiconductor-related companies had different risk and return behavior compared to larger diversified technology companies. Nvidia stood out as the highest-growth stock, while companies such as Apple and Microsoft appeared more stable.

The S&P 500 benchmark helped provide context by showing how the broader market performed compared to individual technology and semiconductor stocks.

## 6. Dashboard Interpretation

The Power BI dashboard was created to make the analysis easier to understand for a non-technical user.

The dashboard includes:

* A ticker dropdown
* A stock price trend chart
* A total return card
* An annualized volatility card
* A risk vs return scatterplot
* A written insight explaining the results

The dashboard helps users quickly compare stock performance, risk, and price trends without needing to read Python code or manually inspect CSV files.

## 7. Why This Analysis Is Useful

A basic stock chart can show whether a stock went up or down, but it does not fully explain risk.

This project adds more value by comparing both return and volatility. A stock with high return may look attractive, but if it also has high volatility, it may have involved larger price swings and greater uncertainty.

This kind of analysis could help a stakeholder understand which stocks had strong growth, which were more stable, and which had higher risk.

## 8. Limitations

This project does not prove why a stock increased or decreased. It only analyzes historical stock price behavior.

External factors such as AI demand, earnings reports, supply chain issues, semiconductor demand, and memory/RAM price changes may have influenced stock performance, but this project does not prove causation.

The analysis is based on historical data and should not be used to predict future stock prices.

## 9. Future Improvements

Future improvements could include:

* Adding quarterly earnings data
* Adding market event annotations
* Adding memory/RAM/DRAM price analysis
* Adding monthly seasonality analysis to the dashboard
* Comparing semiconductor stocks against technology sector ETFs
* Improving the Power BI dashboard layout
* Adding more written business insights
* Creating a final PDF version of the report

## 10. Conclusion

This project shows how Python and Power BI can be used together to create a stock market analysis report. Python was used for data collection, cleaning, and analysis, while Power BI was used to create a stakeholder-friendly dashboard.

The main finding was that Nvidia had the strongest growth during the period analyzed, but that growth came with higher volatility. This shows why it is important to compare both return and risk when analyzing stock performance.
