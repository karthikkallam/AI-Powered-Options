import pandas as pd
import matplotlib.pyplot as plt
from metrics import calculate_performance_metrics

class Backtester:
    """A simple backtester for trading strategies."""
    def __init__(self, initial_balance=10000):
        """
        Initialize the backtester.
        :param initial_balance: Starting balance for the backtesting.
        """
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.positions = []
        self.trade_log = []

    def run_backtest(self, data, position_col='position', price_col='close'):
        """
        Run backtest on the provided data.
        :param data: DataFrame with trading data including a position column.
        :param position_col: The column indicating position (1 for long, -1 for short, 0 for flat).
        :param price_col: The column with asset prices.
        """
        for i in range(1, len(data)):
            if data[position_col].iloc[i] != data[position_col].iloc[i - 1]:
                if data[position_col].iloc[i] == 1:
                    self._open_position(data[price_col].iloc[i], 'buy')
                elif data[position_col].iloc[i] == -1:
                    self._open_position(data[price_col].iloc[i], 'sell')
                elif data[position_col].iloc[i] == 0 and self.positions:
                    self._close_position(data[price_col].iloc[i])

        self._close_all_positions(data[price_col].iloc[-1])

    def _open_position(self, price, action):
        """Open a new trading position."""
        position = {
            'entry_price': price,
            'action': action,
            'balance_before': self.balance
        }
        self.positions.append(position)
        self.trade_log.append(f"Opened {action} position at ${price:.2f}")

    def _close_position(self, price):
        """Close the current position."""
        position = self.positions.pop(0)
        pnl = (price - position['entry_price']) if position['action'] == 'buy' else (position['entry_price'] - price)
        self.balance += pnl
        self.trade_log.append(f"Closed {position['action']} position at ${price:.2f}, P&L: ${pnl:.2f}")

    def _close_all_positions(self, current_price):
        """Close all remaining positions at the last available price."""
        while self.positions:
            self._close_position(current_price)

    def report_results(self):
        """Report the final results of the backtest."""
        print("Backtest complete.")
        print(f"Final Balance: ${self.balance:.2f}")
        return self.trade_log

if __name__ == "__main__":
    # Example placeholder data for backtesting
    data = pd.DataFrame({
        'close': [100, 102, 105, 103, 108, 110, 107, 111],
        'position': [0, 1, 1, 0, -1, -1, 0, 1]
    })
    
    backtester = Backtester()
    backtester.run_backtest(data)
    trade_log = backtester.report_results()

    # Plotting the closing prices for visualization
    plt.plot(data['close'], label='Closing Price')
    plt.title('Backtest Results')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
