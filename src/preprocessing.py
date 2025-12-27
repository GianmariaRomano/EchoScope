import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def load_data(file_path):
    # Load CSV file into a pandas data frame.
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Handle missing and duplicate values.
    df = df.dropna() # Drop null values.
    df = df.drop_duplicates() # Drop duplicate values.
    return df

def scale_features(df, numeric_features):
    # Scale numeric features using StandardScaler.
    scaler = StandardScaler()
    df[numeric_features] = scaler.fit_transform(df[numeric_features])
    return df

def save_data(df, output_path):
    # Save the preprocessed data frame into a .csv file.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to: {output_path}")
