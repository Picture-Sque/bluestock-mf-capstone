import pandas as pd
from pathlib import Path

# Create processed folder if it doesn't exist
Path("data/processed").mkdir(parents=True, exist_ok=True)

datasets = [
    ("01_fund_master.csv", "clean_fund_master.csv"),
    ("03_aum_by_fund_house.csv", "clean_aum_by_fund_house.csv"),
    ("04_monthly_sip_inflows.csv", "clean_monthly_sip_inflows.csv"),
    ("05_category_inflows.csv", "clean_category_inflows.csv"),
    ("06_industry_folio_count.csv", "clean_industry_folio_count.csv"),
    ("09_portfolio_holdings.csv", "clean_portfolio_holdings.csv"),
    ("10_benchmark_indices.csv", "clean_benchmark_indices.csv"),
]

for input_file, output_file in datasets:
    print(f"\nProcessing {input_file}...")

    df = pd.read_csv(f"data/raw/{input_file}")

    # Remove duplicates if any
    df = df.drop_duplicates()

    # Remove completely empty rows if any
    df = df.dropna(how="all")

    # Save processed version
    df.to_csv(
        f"data/processed/{output_file}",
        index=False
    )

    print(f"Saved: {output_file}")
    print(f"Rows: {len(df)}")

print("\nAll remaining datasets processed successfully!")