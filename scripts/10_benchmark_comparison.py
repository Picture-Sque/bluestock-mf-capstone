import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# Create folders if needed
# -----------------------------

os.makedirs("reports/charts", exist_ok=True)

# -----------------------------
# Load Files
# -----------------------------

scorecard = pd.read_csv(
    "outputs/fund_scorecard.csv"
)

nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

# -----------------------------
# Date formatting
# -----------------------------

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# -----------------------------
# Top 5 Funds
# -----------------------------

top5 = scorecard.head(5)["amfi_code"].tolist()

# -----------------------------
# Last 3 Years
# -----------------------------

latest_date = nav["date"].max()
start_date = latest_date - pd.DateOffset(years=3)

nav = nav[nav["date"] >= start_date]

# -----------------------------
# Plot
# -----------------------------

plt.figure(figsize=(14,8))

tracking_results = []

# -----------------------------
# Top Funds
# -----------------------------

for code in top5:

    fund_name = funds.loc[
        funds["amfi_code"] == code,
        "scheme_name"
    ].iloc[0]

    fund_df = nav[
        nav["amfi_code"] == code
    ].copy()

    fund_df = fund_df.sort_values("date")

    # Normalize to 100
    fund_df["growth_index"] = (
        fund_df["nav"]
        / fund_df["nav"].iloc[0]
    ) * 100

    plt.plot(
        fund_df["date"],
        fund_df["growth_index"],
        label=fund_name[:25]
    )

# -----------------------------
# NIFTY50
# -----------------------------

n50 = benchmark[
    benchmark["index_name"] == "NIFTY50"
].copy()

n50 = n50[n50["date"] >= start_date]

n50["growth_index"] = (
    n50["close_value"]
    / n50["close_value"].iloc[0]
) * 100

plt.plot(
    n50["date"],
    n50["growth_index"],
    linewidth=3,
    label="NIFTY50"
)

# -----------------------------
# NIFTY100
# -----------------------------

n100 = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

n100 = n100[n100["date"] >= start_date]

n100["growth_index"] = (
    n100["close_value"]
    / n100["close_value"].iloc[0]
) * 100

plt.plot(
    n100["date"],
    n100["growth_index"],
    linewidth=3,
    label="NIFTY100"
)

# -----------------------------
# Tracking Error
# -----------------------------

n100["benchmark_return"] = (
    n100["close_value"].pct_change()
)

for code in top5:

    fund_name = funds.loc[
        funds["amfi_code"] == code,
        "scheme_name"
    ].iloc[0]

    fund_df = nav[
        nav["amfi_code"] == code
    ][["date","nav"]].copy()

    fund_df["fund_return"] = (
        fund_df["nav"].pct_change()
    )

    merged = pd.merge(
        fund_df,
        n100[
            ["date","benchmark_return"]
        ],
        on="date"
    ).dropna()

    tracking_error = (
        (merged["fund_return"]
         - merged["benchmark_return"]
        ).std()
        * np.sqrt(252)
    )

    tracking_results.append({
        "amfi_code": code,
        "scheme_name": fund_name,
        "tracking_error": tracking_error
    })

# -----------------------------
# Chart Formatting
# -----------------------------

plt.title(
    "Top 5 Funds vs NIFTY50 & NIFTY100 (Last 3 Years)"
)

plt.xlabel("Date")
plt.ylabel("Growth Index (Base = 100)")
plt.legend()
plt.grid(True)

plt.savefig(
    "reports/charts/benchmark_comparison.png",
    bbox_inches="tight"
)

plt.show()

# -----------------------------
# Save Tracking Error
# -----------------------------

tracking_df = pd.DataFrame(
    tracking_results
)

tracking_df.to_csv(
    "outputs/tracking_error.csv",
    index=False
)

print("\nTracking Error Results\n")
print(tracking_df)

print(
    "\nSaved -> reports/charts/benchmark_comparison.png"
)
print(
    "Saved -> outputs/tracking_error.csv"
)