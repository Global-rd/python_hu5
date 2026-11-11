import requests
import pandas as pd
import numpy as np

print("Requests verzió:", requests.__version__)
print("Pandas verzió:", pd.__version__)

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params)

print("HTTP státuszkód:", response.status_code)

data = response.json()

df = pd.DataFrame(data)

print("\nLekért adatok:")
print(df.head())

print("\nDataFrame mérete:")
print(df.shape)

print("\nDataFrame oszlopai:")
print(df.columns)

print("\nÜres cellák száma oszloponként:")
print(df.isnull().sum())

total_market_cap = df["market_cap"].sum()

print("\nA 250 kriptovaluta összesített market cap értéke:")
print(total_market_cap)

top50_df = df.nlargest(50, "current_price")

print("\nTop 50 kriptovaluta current_price alapján:")
print(top50_df[["name", "current_price"]])

top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

print("\nTop 50 rendezve 24 órás árváltozás alapján:")
print(top50_df[["name", "current_price", "price_change_percentage_24h"]])

top50_df["change_direction"] = np.where(
    top50_df["price_change_percentage_24h"] > 0,
    "+",
    np.where(
        top50_df["price_change_percentage_24h"] < 0,
        "-",
        "0"
    )
)

print("\nTop 50 kriptovaluta változási iránya:")
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])