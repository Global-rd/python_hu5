
import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

df = pd.DataFrame(response.json())

print(f"Letöltött kriptovaluták száma: {len(df)}")
print(df[["name", "current_price", "market_cap"]].head())


# Empty cellák száma
print("\nÜres cellák száma:")
print(df.isna().sum())



# Market cap összege
total_market_cap = df["market_cap"].sum()

print("\nMarket cap összege:")
print(total_market_cap)


# 0Top ötven kriptovaluta price  alapján
top50_df = df.sort_values(
    by="current_price",
    ascending=False

).head(50)



print("\nTop 50:")
print(top50_df[["name", "current_price"]])


# Rendezés a 24 órás változáűs alapján
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h"
)

print("\nRendezett top 50:")
print(top50_df[["name", "price_change_percentage_24h"]])


# Árváltozás irányának meghatározása
def change_direction(value):
    if value > 0:
        return "+"
    else:
        return "-"


top50_df["change_direction"] = top50_df[
    "price_change_percentage_24h"
].apply(change_direction)



print(top50_df[
    ["name", "price_change_percentage_24h", "change_direction"]
])
