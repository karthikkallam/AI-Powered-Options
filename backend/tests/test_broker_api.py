import unittest
from unittest.mock import patch, MagicMock
from live_trading.broker_api import place_order

class TestBrokerAPI(unittest.TestCase):
    @patch('live_trading.broker_api.requests.post')
    def test_place_order_success(self, mock_post):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "order_id": "12345"}
        mock_post.return_value = mock_response

        response = place_order("AAPL", "buy", 10)

        self.assertIsNotNone(response)
        self.assertEqual(response['status'], "success")
        self.assertEqual(response['order_id'], "12345")
        mock_post.assert_called_once()

    @patch('live_trading.broker_api.requests.post')
    def test_place_order_failure(self, mock_post):
        # Mock failed API response
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = Exception("Internal Server Error")
        mock_post.return_value = mock_response

        response = place_order("AAPL", "buy", 10)

        self.assertIsNone(response)
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
