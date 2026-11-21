import requests 
import pandas as pd
import numpy as np 

# 1. az endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"
#2. a parameterek egy dictionaryben: kulcs = parameter neve, ertek = amit kuldunk 
params = {
    "vs_currency": "usd",
    "per_page": 250
}
#3. a hivas: url + params
response = requests.get(url, params=params)
print(response.status_code)

data = response.json()      # a valasz tartalma Python adatkent (lista/dict)

df = pd.DataFrame(data)   #dataframe letrehozasa az adatokbol 
print(df)

#1.feladat: ures cellak szama oszloponkent
empty_cells = df.isna().sum()
print(empty_cells)

#2.feladat: market_cap sum 
sum_of_market_cap = df["market_cap"].sum()
print(sum_of_market_cap)

#3. feladat: top50 crypto valuta tarolasa 
top50_df = df.sort_values("current_price", ascending=False).head(50)
print(top50_df)

#4. feladat: top50 csokkeno sorrend
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_df)

#5.feladat - elso resz, arvaltozas iranyanak meghatarozasa
def change_direction_of(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"
#5. feladat - masodik resz, change direction oszlop letrehozasa vektorizalassal
change_direction_vectorized = np.vectorize(change_direction_of)
top50_df["change_direction"] = change_direction_vectorized(top50_df["price_change_percentage_24h"])
print(top50_df)