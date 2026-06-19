import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_stock_data(file_path):
    return pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)


def calculate_monthly_returns(close_prices):
    monthly_prices = close_prices.resample("ME").last()
    monthly_returns = monthly_prices.pct_change() * 100
    return monthly_returns


def calculate_average_monthly_returns(monthly_returns):
    monthly_returns = monthly_returns.copy()
    monthly_returns["Month"] = monthly_returns.index.month_name()

    average_monthly_returns = monthly_returns.groupby("Month").mean()

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    return average_monthly_returns.reindex(month_order)


def save_monthly_seasonality_chart(average_monthly_returns):
    Path("images/charts").mkdir(parents=True, exist_ok=True)

    average_monthly_returns.plot(kind="bar", figsize=(14, 7))
    plt.title("Average Monthly Returns by Stock")
    plt.xlabel("Month")
    plt.ylabel("Average Monthly Return (%)")
    plt.tight_layout()
    plt.savefig("images/charts/monthly_seasonality.png")
    plt.close()


if __name__ == "__main__":
    stock_data = load_stock_data("data/raw/stock_prices.csv")
    close_prices = stock_data["Close"]

    monthly_returns = calculate_monthly_returns(close_prices)
    average_monthly_returns = calculate_average_monthly_returns(monthly_returns)

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    average_monthly_returns.to_csv("data/processed/monthly_seasonality.csv")

    print(average_monthly_returns)

    save_monthly_seasonality_chart(average_monthly_returns)

    print("Monthly seasonality saved to data/processed/monthly_seasonality.csv")
    print("Chart saved to images/charts/monthly_seasonality.png")