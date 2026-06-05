import pandas as pd

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

nifty100 = benchmark[
    benchmark["index_name"] == "NIFTY100"
]

print(nifty100.head())
print()
print(nifty100.tail())