import pandas as pd
import numpy as np

# -----------------------
# Load Data
# -----------------------

nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

results = []

# -----------------------
# Compute Drawdown
# -----------------------

for fund in nav["amfi_code"].unique():

    fund_df = nav[
        nav["amfi_code"] == fund
    ].copy()

    # Running maximum NAV
    fund_df["running_max"] = (
        fund_df["nav"].cummax()
    )

    # Drawdown
    fund_df["drawdown"] = (
        fund_df["nav"]
        / fund_df["running_max"]
        - 1
    )

    # Worst drawdown
    max_dd = fund_df["drawdown"].min()

    # Trough row
    trough_row = fund_df.loc[
        fund_df["drawdown"].idxmin()
    ]

    trough_date = trough_row["date"]

    results.append({
        "amfi_code": fund,
        "max_drawdown": max_dd,
        "trough_date": trough_date
    })

# -----------------------
# Create DataFrame
# -----------------------

mdd_df = pd.DataFrame(results)

# -----------------------
# Merge Fund Details
# -----------------------

mdd_df = mdd_df.merge(
    funds[
        [
            "amfi_code",
            "scheme_name",
            "fund_house"
        ]
    ],
    on="amfi_code",
    how="left"
)

# -----------------------
# Sort Worst First
# -----------------------

mdd_df = mdd_df.sort_values(
    "max_drawdown"
)

# -----------------------
# Save
# -----------------------

mdd_df.to_csv(
    "outputs/max_drawdown.csv",
    index=False
)

print("\nWorst 10 Drawdowns:\n")

print(
    mdd_df[
        [
            "scheme_name",
            "max_drawdown",
            "trough_date"
        ]
    ].head(10)
)

print("\nSaved -> outputs/max_drawdown.csv")