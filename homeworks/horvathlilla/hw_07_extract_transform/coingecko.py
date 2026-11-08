import requests
import pandas as pd
import numpy as np

"""A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” 
húzd le a 250 legnagyobb market cap-pel rendelkező kriptovalutát.
Tárold el ezeket egy dataframe-ben 
és oldd meg a következő feladatokat pandas segítségével:"""

def get_cryptocurrencies():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "per_page": 250}

    response = requests.get(url, params=params).json()

    coins_df = pd.DataFrame(response)

    return coins_df

coins_df = get_cryptocurrencies()

"""1. Határozd meg, hogy a dataframe egyes oszlopaiban 
hány üres cella található és printeld ki."""

empty_cells = coins_df.isnull().sum()

print(empty_cells)

"""2. Határozd meg a teljes dataframe-re 
a market_cap összegét és printeld ki."""

market_cap_sum = coins_df['market_cap'].sum()

print(market_cap_sum)

"""3. Készíts egy új dataframe-et top50_df néven, 
itt csak az első 50 kriptovalutát tárold current_price alapján"""

top50_df = pd.DataFrame(coins_df.sort_values(by='current_price', ascending=False).head(50))

print(top50_df)

"""4. Rendezd a top50_df-et 
price_change_percentage_24h alapján 
csökkenő sorrendbe!"""

print(top50_df.sort_values(by='price_change_percentage_24h', ascending=False))

"""5. Hozz létre egy új oszlopot a top50_df-be
change_direction néven amelynek 3 értéke lehet :

a. Ha a price_change_percentage_24h értéke nagyobb mint 0, 
az oszlop értéke legyen “+”
b. Ha negatív, az oszlop értéke legyen “-“
c. Ha kereken 0, az érték legyen “0”"""

def change_direction(price_change_percentage_24h):
    if price_change_percentage_24h > 0:
        return "+"
    elif price_change_percentage_24h < 0:
        return "-"
    else:
        return "0"

change_direction_vectorized = np.vectorize(change_direction)
top50_df['change_direction'] = change_direction_vectorized(top50_df['price_change_percentage_24h'])

print(top50_df)

