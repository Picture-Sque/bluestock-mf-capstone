import pandas as pd

returns = pd.read_csv("outputs/returns_computed.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

benchmark["date"] = pd.to_datetime(benchmark["date"])
benchmark["market_return"] = benchmark["close_value"].pct_change()

returns["date"] = pd.to_datetime(returns["date"])

# Take SBI Bluechip as example
fund = returns[
    returns["amfi_code"] == 119551
][["date", "daily_return"]]

merged = pd.merge(
    fund,
    benchmark[["date", "market_return"]],
    on="date"
).dropna()

print(
    "Correlation:",
    merged["daily_return"].corr(
        merged["market_return"]
    )
)