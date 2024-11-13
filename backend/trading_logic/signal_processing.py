import numpy as np

def process_signals(data, model_signal_col='model_signal', strategy_signal_col='signal'):
    """
    Combine and process trading signals from different sources (model and strategy).
    
    :param data: DataFrame containing trading data with columns for model and strategy signals.
    :param model_signal_col: The column name for the AI model-generated signals.
    :param strategy_signal_col: The column name for strategy-generated signals.
    :return: DataFrame with combined signals.
    """
    if model_signal_col not in data.columns or strategy_signal_col not in data.columns:
        raise ValueError(f"Columns '{model_signal_col}' and '{strategy_signal_col}' must exist in the DataFrame.")

    # Combine signals: prioritize model signal if both are present
    data['combined_signal'] = np.where(
        data[model_signal_col] != 0,
        data[model_signal_col],
        data[strategy_signal_col]
    )

    # Add position column to indicate holding (1 for long, -1 for short, 0 for no position)
    data['position'] = data['combined_signal'].shift(1).fillna(0)
    return data

def generate_trade_actions(data, position_col='position'):
    """
    Generate trade actions based on position changes.

    :param data: DataFrame containing a position column.
    :param position_col: The column indicating current position.
    :return: DataFrame with trade actions.
    """
    data['trade_action'] = data[position_col].diff().fillna(0)

    data['trade_action'] = data['trade_action'].apply(lambda x: 'buy' if x > 0 else ('sell' if x < 0 else 'hold'))
    return data
