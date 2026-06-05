import pandas as pd

df = pd.read_csv("outputs/returns_computed.csv")

print(df["daily_return"].describe())