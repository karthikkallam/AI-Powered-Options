import logging
import pandas as pd

def save_data_to_csv(data, file_path='market_data.csv'):
    """Save processed market data to a CSV file."""
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
        raise

def load_data_from_csv(file_path='market_data.csv'):
    """Load market data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return df.to_dict(orient='records')
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        raise
    except Exception as e:
        logging.error(f"Error loading data from CSV: {e}")
        raise
