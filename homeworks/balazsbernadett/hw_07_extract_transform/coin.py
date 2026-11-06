import requests
import pandas as pd
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {"vs_currency" : "usd",
              "per_page" : 250
            }

response = requests.get(url=url, params=parameters).json()

df = pd.DataFrame(response)

print(df.head())
print(df.shape)

#1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki
nulls = df.isnull().sum()
print(nulls[nulls > 0])

#2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
print(df["market_cap"].sum())

#3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján

top50_df = df[:50]
print(top50_df)

#4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
result = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(result)
print(result[["name", "price_change_percentage_24h"]])

#5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
#a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
#b. Ha negatív, az oszlop értéke legyen “-“
#c. Ha kereken 0, az érték legyen “0”

def change_direction(price_change_percentage_24h):
  if price_change_percentage_24h > 0:
    return "+"
  if price_change_percentage_24h < 0:
    return "-"
  return 0

change_direction_vectorized = np.vectorize(change_direction)

top50_df["change_direction"] = change_direction_vectorized(top50_df["price_change_percentage_24h"])
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])
