import unittest
from unittest.mock import patch, MagicMock
from live_trading.notifications import send_notification

class TestNotifications(unittest.TestCase):

    @patch('live_trading.notifications.smtplib.SMTP')
    def test_send_notification_success(self, mock_smtp):
        # Mock SMTP instance and behavior
        mock_instance = mock_smtp.return_value.__enter__.return_value
        mock_instance.send_message.return_value = None

        # Call the function to test
        send_notification("Test notification message", "Test Subject", "recipient@example.com")

        # Assert the send_message method was called
        mock_instance.send_message.assert_called_once()

    @patch('live_trading.notifications.smtplib.SMTP')
    def test_send_notification_failure(self, mock_smtp):
        # Simulate an exception during sending
        mock_instance = mock_smtp.return_value.__enter__.return_value
        mock_instance.send_message.side_effect = Exception("SMTP error")

        # Ensure no exception propagates and error is handled
        try:
            send_notification("Test notification message", "Test Subject", "recipient@example.com")
            self.assertTrue(True)  # Passed if no exception
        except Exception:
            self.fail("send_notification raised an exception unexpectedly!")

if __name__ == "__main__":
    unittest.main()
