import pandas as pd
from pathlib import Path

# -------------------------
# File Paths
# -------------------------

INPUT_FILE = "data/raw/02_nav_history.csv"
OUTPUT_FILE = "data/processed/clean_nav_history.csv"

# -------------------------
# Load Dataset
# -------------------------

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows Loaded: {len(df)}")

# -------------------------
# Data Quality Checks
# -------------------------

print("\nChecking missing values...")

print(df.isnull().sum())

print("\nChecking duplicates...")

duplicates = df.duplicated().sum()

print(f"Duplicate Rows: {duplicates}")

print("\nChecking invalid NAV values...")

invalid_nav = (df["nav"] <= 0).sum()

print(f"NAV <= 0 : {invalid_nav}")

# -------------------------
# Convert Date
# -------------------------

print("\nConverting date column...")

df["date"] = pd.to_datetime(df["date"])

# -------------------------
# Sort Data
# -------------------------

print("\nSorting dataset...")

df = df.sort_values(
    by=["amfi_code", "date"]
)

# -------------------------
# Forward Fill NAV
# -------------------------

print("\nForward filling NAV values...")

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
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