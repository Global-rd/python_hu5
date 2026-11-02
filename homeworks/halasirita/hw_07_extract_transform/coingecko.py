import requests
import pandas as pd


def get_change_direction(value):
    if pd.isna(value):
        return None
    elif value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"


# 1. Adatok lekérése a CoinGecko API-ból
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

# 2. DataFrame létrehozása
df = pd.DataFrame(data)

# 3. Hiányzó értékek oszloponként
print("Hiányzó értékek:")
print(df.isna().sum())

# 4. Teljes piaci kapitalizáció
print("\nTeljes piaci kapitalizáció (USD):")
print(df["market_cap"].sum())

# 5. Az 50 legmagasabb árú kriptovaluta
top50_df = df.sort_values(
    "current_price",
    ascending=False
).head(50).copy()

# 6. Rendezés a 24 órás árváltozás szerint
top50_df = top50_df.sort_values(
    "price_change_percentage_24h",
    ascending=False
)

# 7. Árváltozás irányának meghatározása
top50_df["change_direction"] = (
    top50_df["price_change_percentage_24h"]
    .apply(get_change_direction)
)

# 8. Eredmény ellenőrzése
print("\nAz első 5 kriptovaluta:")
print(top50_df.head(5))

