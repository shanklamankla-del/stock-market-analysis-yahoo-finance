import pandas as pd
from pathlib import Path


def load_stock_data(file_path):
    """
    Loads stock price data from a CSV file.
    The CSV has multiple header rows because it came from yfinance.
    """
    data = pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)
    return data


def calculate_daily_returns(close_prices):
    """
    Calculates daily percentage returns.
    """
    daily_returns = close_prices.pct_change()
    return daily_returns


def calculate_total_returns(close_prices):
    """
    Calculates total return for each stock.
    """
    total_returns = (close_prices.iloc[-1] / close_prices.iloc[0] - 1) * 100
    return total_returns


def calculate_volatility(daily_returns):
    """
    Calculates annualized volatility for each stock.
    """
    volatility = daily_returns.std() * (252 ** 0.5) * 100
    return volatility


if __name__ == "__main__":
    file_path = "data/raw/stock_prices.csv"

    stock_data = load_stock_data(file_path)

    close_prices = stock_data["Close"]

    daily_returns = calculate_daily_returns(close_prices)
    total_returns = calculate_total_returns(close_prices)
    volatility = calculate_volatility(daily_returns)

    print("\nTotal Returns (%):")
    print(total_returns.sort_values(ascending=False))

    print("\nAnnualized Volatility (%):")
    print(volatility.sort_values(ascending=False))

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    total_returns.to_csv("data/processed/total_returns.csv")
    volatility.to_csv("data/processed/volatility.csv")

    print("\nAnalysis files saved to data/processed/")