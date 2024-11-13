import unittest
from unittest.mock import patch, MagicMock
from live_trading.live_trader import LiveTrader
from trading_logic.strategy import simple_strategy
from data_acquisition.fetch_data import fetch_live_price

class TestIntegration(unittest.TestCase):

    @patch('live_trading.live_trader.fetch_live_price')
    @patch('live_trading.broker_api.place_order')
    @patch('live_trading.notifications.send_notification')
    def test_live_trading_flow(self, mock_send_notification, mock_place_order, mock_fetch_live_price):
        # Mock data for fetch_live_price
        mock_fetch_live_price.return_value = {
            'close': [100, 102, 105, 103, 108],
            'open': [98, 101, 104, 102, 107],
            'high': [101, 103, 106, 104, 109],
            'low': [97, 100, 103, 101, 106],
            'volume': [1000, 1200, 1500, 1100, 1300]
        }

        # Mock responses for place_order and send_notification
        mock_place_order.return_value = {"status": "success", "order_id": "test123"}
        mock_send_notification.return_value = None

        # Instantiate LiveTrader and run a single iteration of start_trading
        trader = LiveTrader("AAPL", simple_strategy, interval=1)
        trader.start_trading()

        # Assertions to verify interaction between components
        mock_fetch_live_price.assert_called_once_with("AAPL")
        mock_place_order.assert_called()
        mock_send_notification.assert_called()

if __name__ == "__main__":
    unittest.main()
