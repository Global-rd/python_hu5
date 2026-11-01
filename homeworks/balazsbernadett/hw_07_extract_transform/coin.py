import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {"vs_currency" : "usd",
              "per_page" : 250
            }

response = requests.get(url=url, params=parameters).json()

df = pd.DataFrame(response)

print(df.head())
print(df.shape)

#1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki
for column in df.columns:
    empty = df[column].isnull().sum()
    if empty > 0:
        print(column, empty)

#2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
sum_market_cup = 0
for market_cup in df["market_cap"]: 
    sum_market_cup += market_cup

print(sum_market_cup)

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

change_direction = []

for pcp24 in top50_df["price_change_percentage_24h"]:
    if pcp24 > 0:
        change_direction.append("+")
    elif pcp24 < 0:
        change_direction.append("-")
    else:
        change_direction.append("0")

top50_df["change_direction"] = change_direction
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])