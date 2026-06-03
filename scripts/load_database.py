import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# ==================================
# DATABASE CONNECTION
# ==================================

DB_PATH = "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("Database created successfully!")

# ==================================
# LOAD DATASETS
# ==================================

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

nav_df = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

tx_df = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

perf_df = pd.read_csv(
    "data/processed/clean_performance.csv"
)

aum_df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# ==================================
# LOAD TABLES
# ==================================

print("\nLoading dim_fund...")

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded dim_fund")

print("\nLoading fact_nav...")

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded fact_nav")

print("\nLoading fact_transactions...")

tx_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded fact_transactions")

print("\nLoading fact_performance...")

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded fact_performance")

print("\nLoading fact_aum...")

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded fact_aum")

# ==================================
# VERIFY ROW COUNTS
# ==================================

conn = sqlite3.connect(DB_PATH)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\n==============================")
print("ROW COUNT VERIFICATION")
print("==============================")

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS count FROM {table}",
        conn
    )

    print(
        f"{table}: {count['count'][0]} rows"
    )

conn.close()

print("\nDatabase Loading Complete!")