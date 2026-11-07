import requests
import pandas as pd
import numpy as np

#--------------------------------------------------------

url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {"vs_currency": "usd", "per_page": 250}
response = requests.get(url, params=parameters)

if response.status_code == 200:
    df = pd.DataFrame(response.json())
else:
#    print(f"API error: {response.status_code}")
    raise SystemExit(f"\nAPI error: {response.status_code}\n")

#print(response.status_code)

def separator(num):
    print(f"\n#{num}.\n---------------------------------")

#1.
separator(1)
empty_values_per_column = df.isnull().sum()
print(empty_values_per_column)

#2.
separator(2)
total_of_market_cap = df["market_cap"].sum()
print(f"Total Market cap of the first 250 crypto: {total_of_market_cap:,} USD")

#3.
separator(3)
top50_df = df.nlargest(50,"current_price")
print(top50_df[["symbol", "current_price"]])

#4.
separator(4)
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
print(top50_df[["symbol", "price_change_percentage_24h", "current_price"]])

#5.
separator(5)
#top50_df["change_direction"] = pd.NA
choises = ["+", "-", "0"]
condis = [
        top50_df["price_change_percentage_24h"] > 0,
         top50_df["price_change_percentage_24h"] < 0,
         top50_df["price_change_percentage_24h"] == 0,
         ]
top50_df["change_direction"] = np.select(condis, choises, default=None)
print(top50_df[["symbol", "change_direction", "price_change_percentage_24h"]])
