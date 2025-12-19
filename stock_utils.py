import pandas as pd
import numpy as np
from functools import wraps
from stock_pair_class import StockPair


def validate_prices(func):
    """Decorator to validate that price data is numeric and valid."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        df = args[0] if args else kwargs.get('df')
        if df is None:
            raise ValueError("DataFrame is required")
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
         #Took Help From Ai  
        if len(numeric_cols) == 0:
            raise ValueError("No numeric price data found")
        
        if df[numeric_cols].isnull().any().any():
            print("Warning: Missing values detected. Filling with forward fill method.")
            df[numeric_cols] = df[numeric_cols].fillna(method='ffill').fillna(method='bfill')
        
        return func(*args, **kwargs)
    return wrapper


def load_prices(filepath):
    """Load stock prices from CSV file."""
    try:
        df = pd.read_csv(filepath)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date').reset_index(drop=True)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filepath} not found")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


@validate_prices
def calculate_correlation(df):
    """Calculate correlation matrix for all stock pairs."""
    date_col = 'Date' if 'Date' in df.columns else None
    stock_cols = [col for col in df.columns if col != date_col]
    
    price_data = df[stock_cols]
    correlation_matrix = price_data.corr()
    
    return correlation_matrix


def get_correlated_pairs(correlation_matrix, threshold=0.7):
    """Extract strongly correlated stock pairs using list comprehension."""
    stocks = correlation_matrix.columns
    pairs = [
        StockPair(stocks[i], stocks[j], correlation_matrix.iloc[i, j])
        for i in range(len(stocks))
        for j in range(i + 1, len(stocks))
        if abs(correlation_matrix.iloc[i, j]) >= threshold
    ]
    return pairs


def save_analysis(correlation_matrix, output_path):
    """Save correlation matrix to JSON file."""
    correlation_dict = correlation_matrix.to_dict()
    
    import json
    with open(output_path, 'w') as f:
        json.dump(correlation_dict, f, indent=4)
    
    print(f"Correlation matrix saved to {output_path}")
