import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNAV <= 0:")
print((df["nav"] <= 0).sum())

print("\nUnique Funds:")
print(df["amfi_code"].nunique())

df["date"] = pd.to_datetime(df["date"])

print("\nEarliest Date:")
print(df["date"].min())

print("\nLatest Date:")
print(df["date"].max())