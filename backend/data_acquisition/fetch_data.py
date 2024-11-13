import requests
import os

def fetch_market_data():
    """Fetch market data from an external API."""
    api_url = os.getenv('MARKET_DATA_API_URL')
    if not api_url:
        raise ValueError("MARKET_DATA_API_URL is not set in the environment variables.")

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        market_data = response.json()
        return market_data
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching market data: {e}")
