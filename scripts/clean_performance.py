import pandas as pd
from pathlib import Path

INPUT_FILE = "data/raw/07_scheme_performance.csv"
OUTPUT_FILE = "data/processed/clean_performance.csv"

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows Loaded: {len(df)}")

# -------------------------
# Missing Values
# -------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------
# Duplicate Check
# -------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows: {duplicates}")

# -------------------------
# Expense Ratio Validation
# -------------------------

invalid_expense = (
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
).sum()

print(f"\nInvalid Expense Ratios: {invalid_expense}")

# -------------------------
# Sharpe Ratio Anomalies
# -------------------------

sharpe_anomalies = (
    (df["sharpe_ratio"] < -5)
    |
    (df["sharpe_ratio"] > 5)
).sum()

print(f"Sharpe Ratio Anomalies: {sharpe_anomalies}")

# -------------------------
# Beta Anomalies
# -------------------------

beta_anomalies = (
    (df["beta"] < 0)
    |
    (df["beta"] > 3)
).sum()

print(f"Beta Anomalies: {beta_anomalies}")

# -------------------------
# Sort
# -------------------------

df = df.sort_values(
    by=["fund_house", "scheme_name"]
)

# -------------------------
# Remove Duplicates
# -------------------------

df = df.drop_duplicates()

# -------------------------
# Save
# -------------------------

Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaning Complete!")

print(f"Saved to: {OUTPUT_FILE}")

print(f"Final Rows: {len(df)}")