import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/returns_computed.csv")

plt.figure(figsize=(10, 6))

plt.hist(
    df["daily_return"],
    bins=100
)

plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig(
    "reports/charts/daily_return_distribution.png",
    bbox_inches="tight"
)

plt.show()