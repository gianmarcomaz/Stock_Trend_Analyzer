!pip install pandas matplotlib requests

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch stock data
def fetch_stock_data(symbol, period="1mo", interval="1d"):
    df = yf.download(symbol, period=period, interval=interval)
    if df.empty:
        print("Error fetching data")
        return None
    return df

# Function to calculate moving averages
def calculate_moving_averages(df, short_window=20, long_window=50):
    df['SMA_20'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_50'] = df['Close'].rolling(window=long_window).mean()
    return df

# Function to plot stock trends
def plot_stock_trends(df, symbol):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
    plt.plot(df.index, df['SMA_20'], label='20-day SMA', linestyle='dashed', color='orange')
    plt.plot(df.index, df['SMA_50'], label='50-day SMA', linestyle='dashed', color='red')
    plt.legend()
    plt.title(f"Stock Trend Analysis for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.show()

# Example Usage
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Change to any stock ticker
    df = fetch_stock_data(stock_symbol)
    if df is not None:
        df = calculate_moving_averages(df)
        plot_stock_trends(df, stock_symbol)
