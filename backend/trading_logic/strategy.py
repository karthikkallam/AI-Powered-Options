import numpy as np

def simple_moving_average_strategy(data, short_window=5, long_window=20):
    """Implements a simple moving average crossover strategy."""
    if 'close' not in data.columns:
        raise ValueError("Data must include 'close' prices.")

    data['SMA_short'] = data['close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = 0  # Default signal (0 = hold)
    data['signal'][short_window:] = np.where(
        data['SMA_short'][short_window:] > data['SMA_long'][short_window:], 1, -1
    )

    data['position'] = data['signal'].shift(1)  # To avoid look-ahead bias
    return data

def apply_model_predictions(data, model):
    """Apply model predictions to generate trading signals."""
    predictions = model(data[['feature1', 'feature2', 'feature3']].values)
    data['model_signal'] = (predictions > 0.5).float().numpy()  # Convert to 0 or 1
    return data
