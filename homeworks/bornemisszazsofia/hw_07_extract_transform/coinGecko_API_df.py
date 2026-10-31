import requests
import pandas as pd
import numpy as np


url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {"vs_currency": "usd",
              "per_page": 250}
response = requests.get(url=url, params=parameters)
response.raise_for_status()
response_coins = response.json()

#print(response_coins)
#print(type(response_coins))
#print(len(response_coins))

#DataFramebe tarolni a kriptovalutakat: 
df = pd.DataFrame(response_coins)
#print(df)
#print(df.head(5))
#print(df.tail(5))
#df.info()

#1 üres cellak szama oszloponkent:
empty_cells_df = df.isna().sum() #-> True(1)/False(0), then sum
print(empty_cells_df)

#2 market_cap összege:
total_market_cap = df["market_cap"].sum()
print(f"Total market cap value: {total_market_cap:,} USD")

#3 Top50 crypto df:
top50_df = df.sort_values(["current_price"],ascending=False).head(50).reset_index(drop=True)
#print(top50_df)

#4 Top50 price_change_percentage_24h alapjan csökkenö:
top50_df = top50_df.sort_values(["price_change_percentage_24h"], ascending=False).reset_index()
#print(top50_df)

#5 Top50 Uj oszlop:

def price_change_direction(price_change_percentage_24h):
    if pd.isna(price_change_percentage_24h): #guard clause arra az esetre, ha a kesöbbiekbe valtozna a top50 es a 2 ertekkel nem rendelkezö cella belecsuszna a df-be.
        return np.nan
    if price_change_percentage_24h > 0:
        return "+"
    if price_change_percentage_24h < 0:
        return "-"
    if price_change_percentage_24h == 0:
        return "0"

price_change_direction_vectorized = np.vectorize(price_change_direction, otypes=[object])
top50_df["change_direction"] = price_change_direction_vectorized(top50_df["price_change_percentage_24h"])
#print(top50_df)

review_top50_df = top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]]
print(review_top50_df)