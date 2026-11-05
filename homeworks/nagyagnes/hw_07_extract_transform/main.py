import requests
import pandas as pd
import numpy as np
 

# Adatkinyerés: a 250 legnagyobb market cap-pel rendelkező
# kriptovaluta lekérése a CoinGecko public API-ról
# 2 paraméter kell 1 API-hívás

url = "https://api.coingecko.com/api/v3/coins/markets"
 
params = {
    "vs_currency": "usd",
    "per_page": 250
}
 
response = requests.get(url, params=params)
data = response.json()
 
# Az adatok eltárolása dataframeben
df = pd.DataFrame(data)
 

# 1. feladat: üres cellák száma oszloponként

print("--- 1. üres cellák száma oszloponként ---")
print(df.isnull().sum())
 

# 2. feladat: a market_cap összege a teljes dataframe-re

print("--- 2. market_cap összege a teljes dataframe-re ---")
print(df["market_cap"].sum())
 

# 3. feladat: top50_df – az első 50 kriptovaluta current_price alapján 


top50_df = df.sort_values(by="current_price", ascending=False).head(50)
 

# 4. feladat: top50_df rendezése price_change_percentage_24h
# alapján csökkenő sorrendbe

top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)
 

# 5. feladat: change_direction oszlop létrehozása
#   a) > 0  -> "+"
#   b) < 0  -> "-"
#   c) == 0 -> "0"
# (ha az érték hiányzik/ NaN, az oszlop is üres marad)

def change_direction(value):
    if pd.isna(value):
        return None
    elif value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"
 
change_direction_vectorized = np.vectorize(change_direction, otypes=[object])
top50_df["change_direction"] = change_direction_vectorized(
    top50_df["price_change_percentage_24h"]
)
 
print("""--- 3-5. feladatok ---
3. Az első 50 kriptovaluta current_price alapján (top50_df)
4. A top50_df rendezése price_change_percentage_24h szerint csökkenő sorrendbe
5. Új change_direction oszlop: "+", ha pozitív, "-", ha negatív, és "0", ha kereken 0""")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])
 