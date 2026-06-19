import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_stock_data(file_path):
    return pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)


def calculate_quarterly_returns(close_prices):
    quarterly_prices = close_prices.resample("QE").last()
    quarterly_returns = quarterly_prices.pct_change() * 100
    return quarterly_returns


def save_quarterly_returns_chart(quarterly_returns):
    Path("images/charts").mkdir(parents=True, exist_ok=True)

    quarterly_returns.plot(figsize=(14, 7))
    plt.title("Quarterly Stock Returns")
    plt.xlabel("Date")
    plt.ylabel("Quarterly Return (%)")
    plt.tight_layout()
    plt.savefig("images/charts/quarterly_returns.png")
    plt.close()


if __name__ == "__main__":
    stock_data = load_stock_data("data/raw/stock_prices.csv")
    close_prices = stock_data["Close"]

    quarterly_returns = calculate_quarterly_returns(close_prices)

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    quarterly_returns.to_csv("data/processed/quarterly_returns.csv")

    print(quarterly_returns.tail())

    save_quarterly_returns_chart(quarterly_returns)

    print("Quarterly returns saved to data/processed/quarterly_returns.csv")
    print("Chart saved to images/charts/quarterly_returns.png")