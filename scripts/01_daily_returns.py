import pandas as pd
import numpy as np

# Load cleaned NAV data
nav = pd.read_csv("data/processed/clean_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort correctly
nav = nav.sort_values(["amfi_code", "date"])

# Calculate daily return
nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# Remove first null return of each fund
nav["daily_return"] = nav["daily_return"].fillna(0)

# Save output
nav.to_csv(
    "outputs/returns_computed.csv",
    index=False
)

print("Daily returns computed successfully.")
print(nav.head())