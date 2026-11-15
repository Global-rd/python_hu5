import requests
import pandas as pd
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=parameters).json()

df = pd.DataFrame(response) 

print('1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki. ')
print(df.isnull().sum())

print("2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki. ")
print(df['market_cap'].sum())

print('3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján')
top50_df = (df.sort_values(by = 'current_price', ascending = False)
              .reset_index(drop = True)
              .iloc[0:50])

print(top50_df)

print('4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!')
top50_df = top50_df.sort_values(by = 'price_change_percentage_24h', ascending = False)

print('''

5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
    a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen \“+\”
    b. Ha negatív, az oszlop értéke legyen \“-\“
    c. Ha kereken 0, az érték legyen 0
''')

def get_change_direction(pcp):
    if pcp > 0:
        return "+"
    elif pcp < 0:
        return "-"
    else:
        return "0"


get_change_direction_vectorized = np.vectorize(get_change_direction)
top50_df['change direction'] = get_change_direction_vectorized(top50_df['price_change_percentage_24h']) 

print(top50_df.loc[ : , ['id', 'price_change_percentage_24h', 'change direction']])  




