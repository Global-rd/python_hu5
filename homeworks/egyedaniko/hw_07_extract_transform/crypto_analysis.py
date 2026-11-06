"""
Extract & Transform
"""

import requests
import pandas as pd


# Az árváltozás irányának meghatározása
def get_change_direction(change):
    if pd.isna(change):
        return pd.NA

    if change > 0:
        return "+"

    if change < 0:
        return "-"

    return "0"


# API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Két paraméter: USD és 250 kriptovaluta
# Az alapértelmezett rendezés piaci kapitalizáció szerint csökkenő.
params = {
    "vs_currency": "usd",
    "per_page": 250
}

# Adatok lekérése egyetlen API-hívással
try:
    response = requests.get(url, params=params, timeout=30)

    # Hibás HTTP-státusznál kivételt dob
    response.raise_for_status()

    coins = response.json()

except requests.exceptions.RequestException as error:
    print(f"Az API lekérése sikertelen: {error}")
    raise SystemExit(1)

except ValueError as error:
    print(f"Az API válasza nem érvényes JSON: {error}")
    raise SystemExit(1)


# Ellenőrizzük, hogy nem üres listát kaptunk-e
if not isinstance(coins, list) or not coins:
    print("Az API nem adott vissza feldolgozható adatlistát.")
    raise SystemExit(1)


# DataFrame létrehozása
df = pd.DataFrame(coins)

# A feladatokhoz szükséges oszlopok ellenőrzése
required_columns = {
    "name",
    "market_cap",
    "current_price",
    "price_change_percentage_24h"
}

missing_columns = required_columns - set(df.columns)

if missing_columns:
    print(f"Hiányzó oszlopok: {', '.join(sorted(missing_columns))}")
    raise SystemExit(1)


print("\n========== DATAFRAME PREVIEW ==========\n")
print(df.head())
print(f"\nBeolvasott kriptovaluták száma: {len(df)}")


# 1. Üres cellák száma oszloponként
print("\n========== EMPTY CELLS ==========\n")

empty_values = df.isnull().sum()

print(empty_values.to_string())


# 2. A lekért kriptovaluták teljes piaci kapitalizációja
print("\n========== TOTAL MARKET CAP ==========\n")

# A sum alapértelmezetten kihagyja a hiányzó értékeket.
# Ha minden érték hiányzik, a min_count=1 miatt nem ad hamis nullát.
total_market_cap = df["market_cap"].sum(min_count=1)

print(f"Total market cap: {total_market_cap:,.2f} USD")


# 3. Az 50 legmagasabb árú kriptovaluta kiválasztása
top50_df = df.nlargest(50, "current_price").copy()

print("\n========== TOP 50 BY PRICE ==========\n")

print(
    top50_df[["name", "current_price"]].to_string(index=False)
)


# 4. Rendezés a 24 órás árváltozás szerint csökkenően
# A hiányzó értékek a lista végére kerülnek.
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False,
    na_position="last"
)

print("\n========== SORTED TOP 50 ==========\n")

print(
    top50_df[
        ["name", "price_change_percentage_24h"]
    ].to_string(index=False)
)


# 5. Az árváltozás irányát jelző oszlop létrehozása
# Hiányzó változásnál az irány is hiányzó marad.
top50_df["change_direction"] = (
    top50_df["price_change_percentage_24h"]
    .apply(get_change_direction)
)

print("\n========== CHANGE DIRECTION ==========\n")

print(
    top50_df[
        [
            "name",
            "current_price",
            "price_change_percentage_24h",
            "change_direction"
        ]
    ].to_string(index=False)
)
