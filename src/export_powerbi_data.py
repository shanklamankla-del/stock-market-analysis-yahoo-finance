import pandas as pd
from pathlib import Path


def load_stock_data(file_path):
    return pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)


def create_dashboard_data(stock_data):
    close_prices = stock_data["Close"]

    dashboard_data = close_prices.reset_index().melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Close"
    )

    dashboard_data = dashboard_data.dropna(subset=["Close"])

    dashboard_data["Daily_Return"] = (
        dashboard_data.groupby("Ticker")["Close"].pct_change() * 100
    )

    dashboard_data["Year"] = dashboard_data["Date"].dt.year
    dashboard_data["Month"] = dashboard_data["Date"].dt.month_name()
    dashboard_data["Month_Number"] = dashboard_data["Date"].dt.month
    dashboard_data["Quarter"] = dashboard_data["Date"].dt.to_period("Q").astype(str)

    summary = dashboard_data.groupby("Ticker").agg(
        Start_Price=("Close", "first"),
        End_Price=("Close", "last"),
        Average_Daily_Return=("Daily_Return", "mean"),
        Daily_Volatility=("Daily_Return", "std")
    ).reset_index()

    summary["Total_Return_%"] = (
        (summary["End_Price"] / summary["Start_Price"] - 1) * 100
    )

    summary["Annualized_Volatility_%"] = (
        summary["Daily_Volatility"] * (252 ** 0.5)
    )

    summary["Return_to_Risk_Ratio"] = (
        summary["Total_Return_%"] / summary["Annualized_Volatility_%"]
    )

    final_data = dashboard_data.merge(summary, on="Ticker", how="left")

    return final_data


if __name__ == "__main__":
    stock_data = load_stock_data("data/raw/stock_prices.csv")

    dashboard_data = create_dashboard_data(stock_data)

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    dashboard_data.to_csv(
        "data/processed/powerbi_dashboard_data.csv",
        index=False
    )

    print(dashboard_data.head())
    print("Power BI dashboard data saved to data/processed/powerbi_dashboard_data.csv")