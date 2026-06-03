import pandas as pd
from pathlib import Path

# -------------------------
# File Paths
# -------------------------

INPUT_FILE = "data/raw/08_investor_transactions.csv"
OUTPUT_FILE = "data/processed/clean_transactions.csv"

# -------------------------
# Load Dataset
# -------------------------

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows Loaded: {len(df)}")

# -------------------------
# Missing Values Check
# -------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------
# Duplicate Check
# -------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows: {duplicates}")

# -------------------------
# Convert Date
# -------------------------

print("\nConverting transaction_date...")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# -------------------------
# Standardize Transaction Type
# -------------------------

print("\nStandardizing transaction types...")

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
)

# -------------------------
# Validate Amount
# -------------------------

invalid_amounts = (
    df["amount_inr"] <= 0
).sum()

print(f"\nInvalid Amounts: {invalid_amounts}")

# -------------------------
# Validate KYC Status
# -------------------------

valid_kyc = ["Verified", "Pending"]

invalid_kyc = (
    ~df["kyc_status"].isin(valid_kyc)
).sum()

print(f"Invalid KYC Values: {invalid_kyc}")

# -------------------------
# Sort Dataset
# -------------------------

df = df.sort_values(
    by=["transaction_date"]
)

# -------------------------
# Remove Duplicates
# -------------------------

df = df.drop_duplicates()

# -------------------------
# Save Clean Dataset
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