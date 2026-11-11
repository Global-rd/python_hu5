import requests
import pandas as pd
import numpy as np

# getting data from coingecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency": "usd",
    "per_page": 250,
    }
response = requests.get(url, params=parameters)
data = response.json()

# creating a dataframe from the data
coingecko_df = pd.DataFrame(data)
# 1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
print(coingecko_df.isnull().sum())
# 2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
print(coingecko_df['market_cap'].sum())
# Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
top50_df = coingecko_df.nlargest(50, "current_price")
# Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
# Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet
def change_direction(price_change_percentage_24h):
    # Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
    if price_change_percentage_24h > 0:
        return "+"
    # Ha negatív, az oszlop értéke legyen “-“
    elif price_change_percentage_24h < 0:
        return "_"
    # Ha kereken 0, az érték legyen “0”
    else:
        return "no change"

direction_top50_df = np.vectorize(change_direction)
top50_df["change_direction"] = direction_top50_df(top50_df["price_change_percentage_24h"])
print(top50_df)