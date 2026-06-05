import pandas as pd

returns = pd.read_csv("outputs/returns_computed.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

benchmark["market_return"] = (
    benchmark["close_value"].pct_change()
)

print("Fund Return Stats")
print(returns["daily_return"].describe())

print("\nMarket Return Stats")
print(benchmark["market_return"].describe())