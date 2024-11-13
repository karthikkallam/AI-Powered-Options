import os
import requests

# Load environment variables
BROKER_API_URL = os.getenv("BROKER_API_URL", "https://api.broker.com/v1")
API_KEY = os.getenv("BROKER_API_KEY", "your_api_key_here")

def place_order(ticker, action, quantity=1):
    """
    Place an order with the brokerage.
    :param ticker: The stock ticker symbol.
    :param action: The type of order ('buy' or 'sell').
    :param quantity: The number of shares to buy or sell.
    :return: Response from the broker API.
    """
    order_data = {
        "symbol": ticker,
        "action": action,
        "quantity": quantity
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(f"{BROKER_API_URL}/orders", json=order_data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        print(f"Order placed: {action} {quantity} shares of {ticker}. Response: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    result = place_order("AAPL", "buy", 10)
    if result:
        print("Order executed successfully.")
    else:
        print("Failed to execute order.")
