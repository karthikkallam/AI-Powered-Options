import unittest
import pandas as pd
from trading_logic.signal_processing import generate_signals

class TestSignalProcessing(unittest.TestCase):

    def setUp(self):
        # Sample market data for testing
        self.market_data = pd.DataFrame({
            'close': [100, 105, 102, 108, 110],
            'high': [102, 106, 104, 110, 111],
            'low': [98, 101, 100, 107, 108],
            'open': [99, 103, 101, 106, 109],
            'volume': [1000, 1200, 1300, 1100, 1500]
        })

    def test_generate_signals_buy_signal(self):
        # Test for generating a buy signal
        signals = generate_signals(self.market_data)
        self.assertIn('signals', signals.columns)
        self.assertTrue((signals['signals'] == 'buy').any(), "No 'buy' signal found when expected")

    def test_generate_signals_sell_signal(self):
        # Test for generating a sell signal
        self.market_data['close'] = [110, 108, 105, 102, 100]  # Simulate a downward trend
        signals = generate_signals(self.market_data)
        self.assertIn('signals', signals.columns)
        self.assertTrue((signals['signals'] == 'sell').any(), "No 'sell' signal found when expected")

    def test_generate_signals_no_signal(self):
        # Test for generating no signal (neutral)
        self.market_data['close'] = [100, 100, 100, 100, 100]  # Flat trend
        signals = generate_signals(self.market_data)
        self.assertIn('signals', signals.columns)
        self.assertFalse((signals['signals'] == 'buy').any(), "Unexpected 'buy' signal found")
        self.assertFalse((signals['signals'] == 'sell').any(), "Unexpected 'sell' signal found")

if __name__ == "__main__":
    unittest.main()
