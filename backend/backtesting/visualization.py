import matplotlib.pyplot as plt
import pandas as pd

def plot_price_and_positions(data, price_col='close', position_col='position'):
    """
    Plot the closing price of the asset and overlay the positions.
    :param data: DataFrame containing trading data with price and position columns.
    :param price_col: The column with asset prices.
    :param position_col: The column indicating position (1 for long, -1 for short, 0 for flat).
    """
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plot the closing price
    ax1.plot(data.index, data[price_col], label='Close Price', color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.set_title('Price and Trading Positions')

    # Highlight buy and sell positions
    buy_signals = data[data[position_col] == 1]
    sell_signals = data[data[position_col] == -1]

    ax1.scatter(buy_signals.index, buy_signals[price_col], marker='^', color='green', label='Buy', alpha=1)
    ax1.scatter(sell_signals.index, sell_signals[price_col], marker='v', color='red', label='Sell', alpha=1)

    ax1.legend()
    plt.grid(True)
    plt.show()

def plot_cumulative_returns(data, cumulative_return_col='cumulative_return'):
    """
    Plot the cumulative return over the backtesting period.
    :param data: DataFrame containing cumulative return data.
    :param cumulative_return_col: The column with cumulative return data.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data[cumulative_return_col], label='Cumulative Return', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Cumulative Return Over Time')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage with placeholder data
    data = pd.DataFrame({
        'close': [100, 102, 105, 103, 108, 110, 107, 111],
        'position': [0, 1, 1, 0, -1, -1, 0, 1],
        'cumulative_return': [1, 1.02, 1.05, 1.04, 1.08, 1.1, 1.07, 1.11]
    }, index=pd.date_range(start='2024-01-01', periods=8))

    plot_price_and_positions(data)
    plot_cumulative_returns(data)
