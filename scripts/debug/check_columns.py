import pandas as pd

nav = pd.read_csv("data/processed/clean_nav_history.csv")

print("\nNAV Columns:")
print(nav.columns)

benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("\nBenchmark Columns:")
print(benchmark.columns)