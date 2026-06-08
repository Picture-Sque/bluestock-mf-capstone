import pandas as pd

files = {
    "CAGR": "outputs/cagr_report.csv",
    "Sharpe": "outputs/sharpe_values.csv",
    "AlphaBeta": "outputs/alpha_beta.csv",
    "MaxDrawdown": "outputs/max_drawdown.csv"
}

for name, file in files.items():
    df = pd.read_csv(file)
    print(f"{name}: {len(df)} rows")