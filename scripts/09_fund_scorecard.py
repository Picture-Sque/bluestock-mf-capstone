import pandas as pd

# -------------------------
# Load Files
# -------------------------

cagr = pd.read_csv(
    "outputs/cagr_report.csv"
)

sharpe = pd.read_csv(
    "outputs/sharpe_values.csv"
)

alpha_beta = pd.read_csv(
    "outputs/alpha_beta.csv"
)

mdd = pd.read_csv(
    "outputs/max_drawdown.csv"
)

funds = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

# -------------------------
# Merge Everything
# -------------------------

scorecard = (
    cagr
    .merge(
        sharpe[["amfi_code", "sharpe_ratio"]],
        on="amfi_code"
    )
    .merge(
        alpha_beta[["amfi_code", "alpha"]],
        on="amfi_code"
    )
    .merge(
        mdd[["amfi_code", "max_drawdown"]],
        on="amfi_code"
    )
    .merge(
        funds[
            [
                "amfi_code",
                "scheme_name",
                "fund_house",
                "expense_ratio_pct"
            ]
        ],
        on="amfi_code"
    )
)

# -------------------------
# Ranking
# -------------------------

scorecard["return_rank"] = (
    scorecard["cagr_3yr"]
    .rank(pct=True)
)

scorecard["sharpe_rank"] = (
    scorecard["sharpe_ratio"]
    .rank(pct=True)
)

scorecard["alpha_rank"] = (
    scorecard["alpha"]
    .rank(pct=True)
)

# Lower expense better
scorecard["expense_rank"] = (
    (-scorecard["expense_ratio_pct"])
    .rank(pct=True)
)

# Less drawdown better
scorecard["drawdown_rank"] = (
    scorecard["max_drawdown"]
    .rank(pct=True)
)

# -------------------------
# Composite Score
# -------------------------

scorecard["fund_score"] = (
      0.30 * scorecard["return_rank"]
    + 0.25 * scorecard["sharpe_rank"]
    + 0.20 * scorecard["alpha_rank"]
    + 0.15 * scorecard["expense_rank"]
    + 0.10 * scorecard["drawdown_rank"]
) * 100

# -------------------------
# Sort Best First
# -------------------------

scorecard = scorecard.sort_values(
    "fund_score",
    ascending=False
)

# -------------------------
# Save
# -------------------------

scorecard.to_csv(
    "outputs/fund_scorecard.csv",
    index=False
)

print("\nTop 10 Funds\n")

print(
    scorecard[
        [
            "scheme_name",
            "fund_score"
        ]
    ].head(10)
)

print("\nSaved -> outputs/fund_scorecard.csv")