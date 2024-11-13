import numpy as np

class RiskManager:
    """A simple risk management class for trading strategies."""
    def __init__(self, max_position_size=0.1, stop_loss_threshold=0.05, take_profit_threshold=0.1):
        """
        Initialize the risk manager.
        :param max_position_size: Maximum position size as a percentage of the portfolio.
        :param stop_loss_threshold: Stop loss as a percentage of entry price.
        :param take_profit_threshold: Take profit as a percentage of entry price.
        """
        self.max_position_size = max_position_size
        self.stop_loss_threshold = stop_loss_threshold
        self.take_profit_threshold = take_profit_threshold

    def calculate_position_size(self, portfolio_value, entry_price):
        """Calculate the position size based on the portfolio value and maximum position size."""
        position_size = (self.max_position_size * portfolio_value) / entry_price
        return position_size

    def check_stop_loss(self, entry_price, current_price):
        """Check if the stop loss condition is met."""
        return current_price <= entry_price * (1 - self.stop_loss_threshold)

    def check_take_profit(self, entry_price, current_price):
        """Check if the take profit condition is met."""
        return current_price >= entry_price * (1 + self.take_profit_threshold)

    def should_exit_position(self, entry_price, current_price):
        """Determine if the position should be exited based on stop loss or take profit."""
        if self.check_stop_loss(entry_price, current_price):
            return 'stop_loss'
        elif self.check_take_profit(entry_price, current_price):
            return 'take_profit'
        return None
