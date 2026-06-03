import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

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

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())

print("\nAmount Statistics:")
print(df["amount_inr"].describe())

print("\nSample Data:")
print(df.head())