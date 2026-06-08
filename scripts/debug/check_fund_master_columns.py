import pandas as pd

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

print(funds.columns)