import pandas as pd

df = pd.read_csv("outputs/returns_computed.csv")

print(df.columns)
print()
print(df.head())