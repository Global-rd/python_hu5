
import requests
import pandas as pd


# 1. A 250 legnagyobb piaci kapitalizációjú kriptovaluta lekérése

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)


# 2. Üres cellák száma oszloponként

print("Üres cellák száma oszloponként:")
print(df.isnull().sum())


# 3. Teljes piaci kapitalizáció összege

total_market_cap = df["market_cap"].sum()

print("\nA 250 kriptovaluta teljes piaci kapitalizációja:")
print(total_market_cap)


# 4. Az 50 legmagasabb árú kriptovaluta kiválasztása

top50_df = df.sort_values(
    by="current_price",
    ascending=False
).head(50).copy()


# 5. Rendezés a 24 órás százalékos árváltozás alapján

top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)


# 6. Az árváltozás irányának meghatározása

def get_change_direction(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"


top50_df["change_direction"] = top50_df[
    "price_change_percentage_24h"
].apply(get_change_direction)


# 7. Az eredmény megjelenítése

print("\nAz 50 legmagasabb árú kriptovaluta, 24 órás árváltozás szerint rendezve:")

print(
    top50_df[
        [
            "name",
            "symbol",
            "current_price",
            "price_change_percentage_24h",
            "change_direction"
        ]
    ].to_string(index=False)
)
