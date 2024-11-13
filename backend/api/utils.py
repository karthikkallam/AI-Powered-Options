import logging
from datetime import datetime

def setup_logging(log_file='app.log'):
    """Setup logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized.")

def log_request(request):
    """Log incoming API request details."""
    logging.info(f"Request received at {datetime.now()}: {request.method} {request.url}")

def log_response(response):
    """Log outgoing API response details."""
    logging.info(f"Response sent at {datetime.now()}: {response.status_code}")
    return response
