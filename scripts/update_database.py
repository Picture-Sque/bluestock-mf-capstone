import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

sip_df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip_df.to_sql(
    "fact_sip",
    engine,
    if_exists="replace",
    index=False
)

print("fact_sip loaded successfully!")
print(f"Rows Loaded: {len(sip_df)}")