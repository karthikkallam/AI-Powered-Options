import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "your_email@example.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_password")

def send_notification(message, subject="Trading Notification", recipient=None):
    """
    Send an email notification.
    :param message: The message body of the email.
    :param subject: The subject of the email.
    :param recipient: The recipient's email address. Defaults to the sender's address.
    """
    if recipient is None:
        recipient = EMAIL_ADDRESS

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Notification sent to {recipient}.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Example usage
    send_notification("Test notification for trading alert.", "Test Alert")
