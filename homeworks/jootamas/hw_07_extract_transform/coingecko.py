"""
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” húzd le
a 250 legnagyobb market cap-pel rendelkező kriptovalutát.

https://docs.coingecko.com/reference/coins-markets

Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas segítségével
"""

import sys

import numpy as np
import pandas as pd
import requests


def call_api():
  api_endpoint = "https://api.coingecko.com/api/v3/coins/markets"
  api_params = {"vs_currency": "usd", "per_page": 250}

  api_response = requests.get(url=api_endpoint, params=api_params).json()

  # hibakezeles itt nem volt feladat, de egy minimumot beleirok

  # error eseten dict lesz az api_response, success eseten pedig list
  if isinstance(api_response, dict) and isinstance(api_response["error"], str):
    return f"CoinGecko API error: {api_response["error"]}"

  try:
    coins = pd.DataFrame(api_response)
  except ValueError as e:
    return e

  return coins

coins_df = call_api()

# ha hiba volt a lekeressel, akkor ez string

if isinstance(coins_df, str):
  print(coins_df)
  sys.exit()

# megvan a valasz, mehetunk tovabb feldolgozni

# 1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.

empty_cells_df = pd.DataFrame({
  "column": coins_df.columns,
  "empty_cells": [coins_df[col].isna().sum() for col in coins_df.columns] })

print()
print("---------- 1. Üres cellák száma az egyes oszlopokban ----------")
print()
print(empty_cells_df)

# 2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.

# kicsit bonyolitva, de olvashatobban kiirva
market_cap = coins_df["market_cap"].sum()

print()
print(f"---------- 2. Teljes market_cap: {market_cap:,.0f} ----------".replace(",", "."))

# 3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján

# nem irja a feladat, hogy ASC vagy DESC, ezert csokkenore allitottam, a nagyokkal elol

print()
print("---------- 3. Az első 50 kriptovaluta aktuális ár szerinti sorrendben ----------")
print()

top50_df = pd.DataFrame(coins_df.sort_values("current_price", ascending=False).head(50))

print(top50_df)

# 4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!

print()
print("---------- 4. Az első 50 kriptovaluta 24h változás szerint csökkenő sorrendben ----------")
print()

print(top50_df.sort_values("price_change_percentage_24h", ascending=False))

# 5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet:
# a) Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
# b) Ha negatív, az oszlop értéke legyen “-“
# c) Ha kereken 0, az érték legyen “0”

print()
print("---------- 5. Új oszlop a top50_df-ben: change_direction ----------")
print()

def change_direction(price_change_percentage_24h):
  if price_change_percentage_24h > 0:
    return "+"
  if price_change_percentage_24h < 0:
    return "-"
  return 0

change_direction_vectorized = np.vectorize(change_direction)

top50_df["change_direction"] = change_direction_vectorized(top50_df["price_change_percentage_24h"])

print(top50_df)
