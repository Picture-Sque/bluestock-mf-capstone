import pandas as pd
from pathlib import Path

# ==========================
# LOAD DATA
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

processed_path = BASE_DIR / "data" / "processed"

funds = pd.read_csv(processed_path / "clean_fund_master.csv")
performance = pd.read_csv(processed_path / "clean_performance.csv")

print("Files loaded successfully")

# ==========================
# MERGE DATASETS
# ==========================

df = funds.merge(
    performance,
    on="amfi_code",
    how="inner",
    suffixes=("_fund", "_perf")
)

# ==========================
# RISK MAPPING
# ==========================

risk_map = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Very High"]
}

# ==========================
# RECOMMENDATION FUNCTION
# ==========================

def recommend_funds(risk_appetite):

    allowed_risk = risk_map.get(risk_appetite)

    if allowed_risk is None:
        print("Invalid Risk Appetite!")
        print("Choose: Low / Moderate / High")
        return

    filtered = df[
        df["risk_category"].isin(allowed_risk)
    ].copy()

    recommendations = (
        filtered
        .sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print("\n")
    print("=" * 80)
    print(f"TOP 3 FUNDS FOR {risk_appetite.upper()} RISK INVESTORS")
    print("=" * 80)

    print(
        recommendations[
            [
                "scheme_name_fund",
                "fund_house_fund",
                "risk_category",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ]
        .rename(
            columns={
                "scheme_name_fund": "Fund Name",
                "fund_house_fund": "Fund House",
                "risk_category": "Risk",
                "sharpe_ratio": "Sharpe Ratio",
                "return_3yr_pct": "3Y Return (%)"
            }
        )
        .to_string(index=False)
    )

# ==========================
# DEMO RUNS
# ==========================

recommend_funds("Low")
recommend_funds("Moderate")
recommend_funds("High")