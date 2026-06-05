import pandas as pd
import numpy as np

# -----------------------
# Load Data
# -----------------------

returns = pd.read_csv(
    "outputs/returns_computed.csv"
)

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

# -----------------------
# Risk Free Rate
# -----------------------

RF_ANNUAL = 0.065
RF_DAILY = RF_ANNUAL / 252

results = []

# -----------------------
# Sharpe Calculation
# -----------------------

for fund in returns["amfi_code"].unique():

    fund_returns = returns[
        returns["amfi_code"] == fund
    ]["daily_return"]

    mean_return = fund_returns.mean()

    std_return = fund_returns.std()

    sharpe = (
        (mean_return - RF_DAILY)
        / std_return
    ) * np.sqrt(252)

    results.append({
        "amfi_code": fund,
        "sharpe_ratio": sharpe
    })

# -----------------------
# Convert to DataFrame
# -----------------------

sharpe_df = pd.DataFrame(results)

# -----------------------
# Merge Fund Details
# -----------------------

sharpe_df = sharpe_df.merge(
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
# Rank Funds
# -----------------------

sharpe_df = sharpe_df.sort_values(
    "sharpe_ratio",
    ascending=False
)

# -----------------------
# Save
# -----------------------

sharpe_df.to_csv(
    "outputs/sharpe_values.csv",
    index=False
)

print("\nTop 10 Funds by Sharpe Ratio:\n")
print(
    sharpe_df[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio"
        ]
    ].head(10)
)

print("\nSaved -> outputs/sharpe_values.csv")