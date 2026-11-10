
import os
import requests
import pandas as pd
import numpy as np

# PANDAS BEALLITASOK
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. API ADATOK LEKERESE
url = "https://api.coingecko.com/api/v3/coins/markets"

print("Elo kriptovaluta-adatok lekerese a CoinGecko API-rol...")

try:
    response = requests.get(
        url,
        params={
            "vs_currency": "usd",
            "per_page": 250
        },
        timeout=15
    )

    response.raise_for_status()
    json_data = response.json()

    if not json_data:
        raise ValueError("Az API nem adott vissza kriptovaluta-adatokat.")

    # API ADATOK BETOLTESE DATAFRAME-BE
    df = pd.DataFrame(json_data)

    print("Sikeres API lekeres!")
    print(f"Feldolgozott kriptovalutak szama: {len(df)}\n")

except (requests.exceptions.RequestException, ValueError) as e:
    print(f"Hiba tortent az API lekerese soran: {e}")
    print("A program leall.")
    raise SystemExit(1)


# 2. FELADAT: URES CELLÁK MEGHATAROZASA
print("--- 1. Feladat: Ures cellak szama oszloponkent ---")

missing_values = df.isnull().sum()

print(missing_values)
print("\n")


# 3. FELADAT: MARKET CAP TELJES OSSZEGE
print("--- 2. Feladat: Teljes market_cap osszeg ---")

total_market_cap = df["market_cap"].sum()

print(f"A teljes market cap osszege: {total_market_cap:,.2f} USD")
print("\n")


# 4. FELADAT: TOP 50 KRIPTOVALUTA KIVALASZTASA
print("--- 3. Feladat: top50_df letrehozasa ---")

top50_df = df.sort_values(
    by="current_price",
    ascending=False
).head(50).copy()

print(f"A top50_df letrejott. Sorok szama: {len(top50_df)}")
print("\n")


# 5. FELADAT: RENDEZES 24 ORAS ARVALTOZAS ALAPJAN
print("--- 4. Feladat: top50_df rendezese ---")

top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

print(
    top50_df[
        ["name", "current_price", "price_change_percentage_24h"]
    ].head()
)

print("\n")


# 6. FELADAT: CHANGE_DIRECTION OSZLOP LETREHOZASA
print("--- 5. Feladat: change_direction oszlop ---")

conditions = [
    top50_df["price_change_percentage_24h"] > 0,
    top50_df["price_change_percentage_24h"] < 0,
    top50_df["price_change_percentage_24h"] == 0
]

choices = ["+", "-", "0"]

top50_df["change_direction"] = np.select(
    conditions,
    choices,
    default="NaN"
)

print(
    top50_df[
        ["name", "price_change_percentage_24h", "change_direction"]
    ].head(10)
)

print("\n")


# 7. FELADAT: CSV MENTES
print("--- Eredmenyek mentese fajlba ---")

current_dir = os.path.dirname(os.path.abspath(__file__))

output_path = os.path.join(
    current_dir,
    "top50_kripto.csv"
)

top50_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(f"Sikeresen elmentve ide: {output_path}")
