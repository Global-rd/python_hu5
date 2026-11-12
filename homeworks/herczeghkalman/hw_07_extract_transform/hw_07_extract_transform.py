
import urllib.request
import json
import pandas as pd

# Adatok lekérése a CoinGecko API-ról (250 legnagyobb market cap-pel rendelkező kriptovaluta)
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250"

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf-8"))

# Lekért adatok tárolása DataFrame-ben
df = pd.DataFrame(data)

# 1. feladat: Üres cellák számának meghatározása oszloponként
print("1. feladat - Üres cellák száma oszloponként:")
print(df.isnull().sum())

# 2. feladat: A teljes DataFrame market_cap értékeinek összege
print("\n2. feladat - Teljes market cap:")
print(df["market_cap"].sum())

# 3. feladat: Top 50 kriptovaluta kiválasztása current_price alapján
top50_df = df.nlargest(50, "current_price").copy()

# 4. feladat: Rendezés price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

# 5. feladat: change_direction oszlop létrehozása
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    lambda x: "+" if x > 0 else ("-" if x < 0 else "0")
)

# Eredmény megjelenítése
print("\nTop 50 DataFrame:")
print(top50_df[["name", "symbol", "current_price",
                "price_change_percentage_24h", "change_direction"]])
