import pandas as pd
import requests

#Kriptovaluták letöltése
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 250,
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

df = pd.DataFrame(response.json())
print(f"Letöltött kriptovaluták száma: {len(df)}")

#Hiányzó cellák oszloponkénti megszámolása
print("\n1. Hiányzó értékek száma oszloponként:")
print(df.isna().sum())

#Letöltött táblázat piaci kapitalizációjának összegzése
total_market_cap = df["market_cap"].sum()
print(f"\n2. A market_cap összege: {total_market_cap:,.2f} USD")

#50 legmagasabb aktuális árú kriptovaluta
top50_df = (
    df.sort_values("current_price", ascending=False)
    .head(50)
    .copy()
)

#Rendezés napi százalékos változás alapján
top50_df = top50_df.sort_values(
    "price_change_percentage_24h",
    ascending=False,
)

#Változás irányát jelző oszlop hozzáadása és az eredmény kiírása
top50_df["change_direction"] = pd.NA

change = top50_df["price_change_percentage_24h"]

top50_df.loc[change > 0, "change_direction"] = "+"
top50_df.loc[change < 0, "change_direction"] = "-"
top50_df.loc[change == 0, "change_direction"] = "0"

print(
    top50_df[
        [
            "name",
            "symbol",
            "current_price",
            "price_change_percentage_24h",
            "change_direction",
        ]
    ].to_string(index=False)
)