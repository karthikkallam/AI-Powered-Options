import pandas as pd
import yfinance as yf

def fetch_historical_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    :param ticker: The stock ticker symbol (e.g., 'AAPL').
    :param start_date: The start date for fetching data (YYYY-MM-DD).
    :param end_date: The end date for fetching data (YYYY-MM-DD).
    :return: A DataFrame containing historical stock data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError("No data returned. Check the ticker symbol or date range.")
        return data[['Open', 'High', 'Low', 'Close', 'Volume']]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    
    data = fetch_historical_data(ticker, start_date, end_date)
    if not data.empty:
        print(data.head())
    else:
        print("No data fetched.")
