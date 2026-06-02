import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching {fund_name}...")

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{fund_name}.csv"

    df.to_csv(
        file_name,
        index=False
    )

    print(f"Saved: {file_name}")

print("\nAll funds downloaded successfully")