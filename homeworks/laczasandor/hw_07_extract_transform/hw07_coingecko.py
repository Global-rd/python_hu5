"""
7. házi feladat – Extract & Transform
CoinGecko public API -> pandas DataFrame -> elemzés
"""
 
import numpy as np
import pandas as pd
import requests
 
# ---------------------------------------------------------------------------
# EXTRACT – 250 legnagyobb market cap-pel rendelkező kriptovaluta
# ---------------------------------------------------------------------------
URL = "https://api.coingecko.com/api/v3/coins/markets"
 
# Két paraméter elég:
#   vs_currency – kötelező, ebben a pénznemben kapjuk az árakat (usd)
#   per_page    – alapból 100, max 250 -> így 1 hívásból megvan mind a 250
# A rendezés alapértelmezetten "market_cap_desc", ezért ezt nem kell megadni.
params = {
    "vs_currency": "usd",
    "per_page": 250,
}
 
response = requests.get(URL, params=params, timeout=30)
response.raise_for_status()  # ha nem 200-as a válasz (pl. 429 rate limit), hibát dob
 
data = response.json()  # lista, benne 250 dict (1 dict = 1 coin)
df = pd.DataFrame(data)
 
print(f"Letöltött sorok száma: {len(df)}")
print()
 
# ---------------------------------------------------------------------------
# 1. Üres cellák száma oszloponként
# ---------------------------------------------------------------------------
print("1. Üres cellák oszloponként:")
print(df.isna().sum())
print()
 
# ---------------------------------------------------------------------------
# 2. A teljes market_cap összege
# ---------------------------------------------------------------------------
total_market_cap = df["market_cap"].sum()
print(f"2. Teljes market cap: {total_market_cap:,.0f} USD")
print()
 
# ---------------------------------------------------------------------------
# 3. top50_df – az első 50 kriptovaluta current_price alapján (legdrágábbak)
# ---------------------------------------------------------------------------
top50_df = df.nlargest(50, "current_price").copy()
# .copy(): önálló DataFrame lesz, így az 5. pontban az új oszlop hozzáadásakor
# nem kapunk SettingWithCopyWarning-ot
 
print("3. top50_df (current_price szerint):")
print(top50_df[["name", "symbol", "current_price"]])
print()
 
# ---------------------------------------------------------------------------
# 4. Rendezés price_change_percentage_24h szerint csökkenő sorrendbe
# ---------------------------------------------------------------------------
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
 
print("4. top50_df price_change_percentage_24h szerint csökkenő sorrendben:")
print(top50_df[["name", "price_change_percentage_24h"]])
print()
 
# ---------------------------------------------------------------------------
# 5. change_direction oszlop: "+", "-" vagy "0"
# ---------------------------------------------------------------------------
change = top50_df["price_change_percentage_24h"]
 
conditions = [
    change > 0,
    change < 0,
    change == 0,
]
choices = ["+", "-", "0"]
 
# np.select sorban végignézi a feltételeket, és az első igaz feltételhez
# tartozó értéket adja. Ha egyik sem igaz (pl. hiányzó / NaN érték),
# akkor a default kerül be.
top50_df["change_direction"] = np.select(conditions, choices, default=None)
 
print("5. top50_df change_direction oszloppal:")
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])
