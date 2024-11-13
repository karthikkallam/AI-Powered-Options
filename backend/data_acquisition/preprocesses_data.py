import pandas as pd

def preprocess_data(raw_data):
    """Preprocess raw market data for analysis."""
    if not raw_data:
        raise ValueError("No data provided for preprocessing.")

    try:
        # Convert raw data into a DataFrame
        df = pd.DataFrame(raw_data)

        # Basic data cleaning
        df.dropna(inplace=True)  # Remove rows with missing values
        df['date'] = pd.to_datetime(df['date'])  # Ensure 'date' column is datetime type
        df.sort_values(by='date', inplace=True)

        # Feature engineering: add moving average as a feature
        df['moving_avg'] = df['close'].rolling(window=5).mean()

        # Normalize price columns (example: 'open', 'high', 'low', 'close')
        price_columns = ['open', 'high', 'low', 'close']
        for col in price_columns:
            df[f'{col}_normalized'] = (df[col] - df[col].mean()) / df[col].std()

        return df.to_dict(orient='records')
    except Exception as e:
        raise RuntimeError(f"Error during data preprocessing: {e}")
