import time
import requests
from broker_api import place_order
from notifications import send_notification
from data_acquisition.fetch_data import fetch_live_price
from trading_logic.signal_processing import process_signals

class LiveTrader:
    """Class for handling live trading operations."""
    def __init__(self, ticker, strategy, interval=60):
        """
        Initialize the live trader.
        :param ticker: The stock ticker symbol to trade.
        :param strategy: The strategy function that determines signals.
        :param interval: Time interval for checking new data in seconds.
        """
        self.ticker = ticker
        self.strategy = strategy
        self.interval = interval

    def start_trading(self):
        """Start the live trading process."""
        print(f"Starting live trading for {self.ticker} with an interval of {self.interval} seconds.")
        while True:
            try:
                price_data = fetch_live_price(self.ticker)
                if price_data.empty:
                    print("Failed to fetch live price data. Skipping iteration.")
                    time.sleep(self.interval)
                    continue

                signal_data = self.strategy(price_data)
                processed_data = process_signals(signal_data)

                if processed_data['trade_action'].iloc[-1] == 'buy':
                    place_order(self.ticker, 'buy')
                    send_notification(f"Executed a buy order for {self.ticker}.")
                elif processed_data['trade_action'].iloc[-1] == 'sell':
                    place_order(self.ticker, 'sell')
                    send_notification(f"Executed a sell order for {self.ticker}.")

                time.sleep(self.interval)

            except Exception as e:
                print(f"An error occurred during live trading: {e}")
                time.sleep(self.interval)

if __name__ == "__main__":
    from trading_logic.strategy import simple_strategy

    ticker = "AAPL"
    trader = LiveTrader(ticker, simple_strategy)
    trader.start_trading()
