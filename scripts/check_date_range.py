import pandas as pd

nav = pd.read_csv("data/processed/clean_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

print("Start Date :", nav["date"].min())
print("End Date   :", nav["date"].max())
print("Unique Funds :", nav["amfi_code"].nunique())