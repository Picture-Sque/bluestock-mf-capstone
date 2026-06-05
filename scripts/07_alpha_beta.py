import pandas as pd
import numpy as np
from scipy.stats import linregress

# -----------------------------
# Load Files
# -----------------------------

returns = pd.read_csv(
    "outputs/returns_computed.csv"
)

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

# -----------------------------
# Prepare Benchmark
# -----------------------------

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

benchmark = benchmark.sort_values("date")

benchmark["market_return"] = (
    benchmark["close_value"]
    .pct_change()
)

benchmark = benchmark[
    ["date", "market_return"]
]

# -----------------------------
# Prepare Fund Returns
# -----------------------------

returns["date"] = pd.to_datetime(
    returns["date"]
)

results = []

# -----------------------------
# Alpha Beta Calculation
# -----------------------------

for fund in returns["amfi_code"].unique():

    fund_df = returns[
        returns["amfi_code"] == fund
    ][["date", "daily_return"]]

    merged = pd.merge(
        fund_df,
        benchmark,
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    if len(merged) < 30:
        continue

    regression = linregress(
        merged["market_return"],
        merged["daily_return"]
    )

    beta = regression.slope

    alpha = regression.intercept * 252

    results.append({
        "amfi_code": fund,
        "alpha": alpha,
        "beta": beta
    })

# -----------------------------
# Create DataFrame
# -----------------------------

alpha_beta_df = pd.DataFrame(results)

# -----------------------------
# Merge Fund Details
# -----------------------------

alpha_beta_df = alpha_beta_df.merge(
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

# -----------------------------
# Sort by Alpha
# -----------------------------

alpha_beta_df = alpha_beta_df.sort_values(
    "alpha",
    ascending=False
)

# -----------------------------
# Save
# -----------------------------

alpha_beta_df.to_csv(
    "outputs/alpha_beta.csv",
    index=False
)

print("\nTop 10 Funds by Alpha\n")

print(
    alpha_beta_df[
        [
            "scheme_name",
            "alpha",
            "beta"
        ]
    ].head(10)
)

print("\nSaved -> outputs/alpha_beta.csv")