import pandas as pd

df = pd.read_csv(
    "outputs/max_drawdown.csv"
)

print(df.tail(5))