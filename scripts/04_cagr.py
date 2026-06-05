import pandas as pd
import numpy as np

# Load NAV data
nav = pd.read_csv("data/processed/clean_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(["amfi_code", "date"])

# Latest date in dataset
latest_date = nav["date"].max()

results = []

for fund in nav["amfi_code"].unique():

    fund_df = nav[nav["amfi_code"] == fund].copy()

    fund_df = fund_df.sort_values("date")

    latest_nav = fund_df.iloc[-1]["nav"]

    # ------------------
    # 1 YEAR CAGR
    # ------------------

    one_year_date = latest_date - pd.DateOffset(years=1)

    one_year_data = fund_df[fund_df["date"] >= one_year_date]

    cagr_1yr = np.nan

    if len(one_year_data) > 0:

        start_nav = one_year_data.iloc[0]["nav"]

        cagr_1yr = (
            (latest_nav / start_nav) ** (1 / 1)
        ) - 1

    # ------------------
    # 3 YEAR CAGR
    # ------------------

    three_year_date = latest_date - pd.DateOffset(years=3)

    three_year_data = fund_df[
        fund_df["date"] >= three_year_date
    ]

    cagr_3yr = np.nan

    if len(three_year_data) > 0:

        start_nav = three_year_data.iloc[0]["nav"]

        cagr_3yr = (
            (latest_nav / start_nav) ** (1 / 3)
        ) - 1

    results.append({
        "amfi_code": fund,
        "cagr_1yr": cagr_1yr,
        "cagr_3yr": cagr_3yr
    })

# Save result
cagr_df = pd.DataFrame(results)

cagr_df.to_csv(
    "outputs/cagr_report.csv",
    index=False
)

print(cagr_df.head())
print("\nSaved -> outputs/cagr_report.csv")