import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        file_path = os.path.join(folder, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 70)
            print(f"FILE: {file}")
            print("=" * 70)

            print("\nSHAPE:")
            print(df.shape)

            print("\nDTYPES:")
            print(df.dtypes)

            print("\nHEAD:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")