import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_stock_data(file_path):
    data = pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)
    return data


def save_stock_price_chart(close_prices):
    Path("images/charts").mkdir(parents=True, exist_ok=True)

    close_prices.plot(figsize=(12, 6))
    plt.title("Stock Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.tight_layout()
    plt.savefig("images/charts/stock_prices_over_time.png")
    plt.close()


def save_total_returns_chart(total_returns):
    Path("images/charts").mkdir(parents=True, exist_ok=True)

    total_returns.sort_values().plot(kind="barh", figsize=(10, 6))
    plt.title("Total Returns by Stock")
    plt.xlabel("Total Return (%)")
    plt.ylabel("Ticker")
    plt.tight_layout()
    plt.savefig("images/charts/total_returns.png")
    plt.close()


def save_volatility_chart(volatility):
    Path("images/charts").mkdir(parents=True, exist_ok=True)

    volatility.sort_values().plot(kind="barh", figsize=(10, 6))
    plt.title("Annualized Volatility by Stock")
    plt.xlabel("Volatility (%)")
    plt.ylabel("Ticker")
    plt.tight_layout()
    plt.savefig("images/charts/volatility.png")
    plt.close()


if __name__ == "__main__":
    stock_data = load_stock_data("data/raw/stock_prices.csv")

    close_prices = stock_data["Close"]

    total_returns = pd.read_csv(
        "data/processed/total_returns.csv",
        index_col=0
    ).squeeze("columns")

    volatility = pd.read_csv(
        "data/processed/volatility.csv",
        index_col=0
    ).squeeze("columns")

    save_stock_price_chart(close_prices)
    save_total_returns_chart(total_returns)
    save_volatility_chart(volatility)

    print("Charts saved to images/charts/")