import yfinance as yf
from pathlib import Path


def download_stock_data(tickers, start_date, end_date):
    # Downloads stock price data from Yahoo Finance.
    data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    threads=False,
    progress=True
    )
    return data


def save_data(data, file_path):
    # Saves the data to a CSV file.
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path)


if __name__ == "__main__":
    tickers = ["NVDA", "AMD", "MU", "AAPL", "MSFT", "AMZN", "^GSPC"]
    start_date = "2020-01-01"
    end_date = "2026-01-01"
    save_path = "data/raw/stock_prices.csv"

    stock_data = download_stock_data(tickers, start_date, end_date)

    print(stock_data.head())

    save_data(stock_data, save_path)
    print(f"Stock data saved to {save_path}")