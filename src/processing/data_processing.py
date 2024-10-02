import pandas as pd

def clean_data(data):
    # Basic data cleaning logic
    return data.dropna()

def load_data(filepath):
    return pd.read_csv(filepath)

# Example usage
if __name__ == "__main__":
    filepath = 'data/raw/city_data.csv'
    data = load_data(filepath)
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
