import pandas as pd
import numpy as np

def calculate_performance_metrics(data, position_col='position', price_col='close'):
    """
    Calculate key performance metrics for a backtest.
    :param data: DataFrame containing trading data with position and price columns.
    :param position_col: The column indicating position (1 for long, -1 for short, 0 for flat).
    :param price_col: The column with asset prices.
    :return: A dictionary of performance metrics.
    """
    # Calculate daily returns based on position changes
    data['daily_return'] = data[position_col].shift(1) * (data[price_col].pct_change())
    data['cumulative_return'] = (1 + data['daily_return']).cumprod()

    # Calculate maximum drawdown
    data['cumulative_max'] = data['cumulative_return'].cummax()
    data['drawdown'] = (data['cumulative_return'] - data['cumulative_max']) / data['cumulative_max']
    max_drawdown = data['drawdown'].min()

    # Calculate annualized return and volatility
    total_return = data['cumulative_return'].iloc[-1] - 1
    annualized_return = (1 + total_return) ** (252 / len(data)) - 1
    annualized_volatility = data['daily_return'].std() * np.sqrt(252)

    # Sharpe ratio (assume risk-free rate is 0)
    sharpe_ratio = annualized_return / annualized_volatility if annualized_volatility != 0 else np.nan

    metrics = {
        'Total Return': total_return,
        'Annualized Return': annualized_return,
        'Annualized Volatility': annualized_volatility,
        'Max Drawdown': max_drawdown,
        'Sharpe Ratio': sharpe_ratio
    }

    return metrics

if __name__ == "__main__":
    # Example usage with placeholder data
    data = pd.DataFrame({
        'close': [100, 102, 105, 103, 108, 110, 107, 111],
        'position': [0, 1, 1, 0, -1, -1, 0, 1]
    })

    metrics = calculate_performance_metrics(data)
    for key, value in metrics.items():
        print(f"{key}: {value:.2%}")
