import pandas as pd
from pathlib import Path


def load_stock_data(file_path):
    return pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)


def create_powerbi_stock_prices(stock_data):
    close_prices = stock_data["Close"]

    long_data = close_prices.reset_index().melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Close"
    )

    long_data["Daily_Return"] = long_data.groupby("Ticker")["Close"].pct_change() * 100
    long_data["Year"] = long_data["Date"].dt.year
    long_data["Month"] = long_data["Date"].dt.month_name()
    long_data["Quarter"] = long_data["Date"].dt.to_period("Q").astype(str)

    return long_data


def create_summary_table(powerbi_data):
    summary = powerbi_data.groupby("Ticker").agg(
        Start_Price=("Close", "first"),
        End_Price=("Close", "last"),
        Average_Daily_Return=("Daily_Return", "mean"),
        Daily_Volatility=("Daily_Return", "std")
    ).reset_index()

    summary["Total_Return_%"] = (
        (summary["End_Price"] / summary["Start_Price"] - 1) * 100
    )

    summary["Annualized_Volatility_%"] = summary["Daily_Volatility"] * (252 ** 0.5)

    return summary


if __name__ == "__main__":
    stock_data = load_stock_data("data/raw/stock_prices.csv")

    powerbi_data = create_powerbi_stock_prices(stock_data)
    summary = create_summary_table(powerbi_data)

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    powerbi_data.to_csv("data/processed/powerbi_stock_prices.csv", index=False)
    summary.to_csv("data/processed/powerbi_stock_summary.csv", index=False)

    print(powerbi_data.head())
    print(summary)

    print("Power BI files saved to data/processed/")