import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("Columns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())