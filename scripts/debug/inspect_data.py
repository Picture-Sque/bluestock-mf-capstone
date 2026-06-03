import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

files = DATA_PATH.glob("*.csv")

for file in files:
    print("\n" + "="*60)
    print(f"FILE: {file.name}")
    print("="*60)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())