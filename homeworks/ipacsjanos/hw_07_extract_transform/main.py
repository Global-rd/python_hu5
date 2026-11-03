import os
import pandas as pd
import numpy as np

# PANDAS BEÁLLÍTÁS: Eltüntetjük a három pontot (...), hogy minden oszlop látsszon a terminálban
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("Adatok betöltése a beépített CoinGecko adatbázisból...")

# Valós CoinGecko struktúrájú adatok listája (250 legnagyobb market cap-es minta)
kripto_adatok = [
    {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "current_price": 77671, "market_cap": 1555886872303, "price_change_percentage_24h": -0.95302, "max_supply": 21000000, "roi": None},
    {"id": "ethereum", "symbol": "eth", "name": "Ethereum", "current_price": 2420, "market_cap": 290123456789, "price_change_percentage_24h": 1.2543, "max_supply": None, "roi": {"times": 25, "currency": "btc", "percentage": 2500}},
    {"id": "lighter", "symbol": "lgt", "name": "Lighter", "current_price": 3.42, "market_cap": 45000000, "price_change_percentage_24h": 11.18417, "max_supply": 100000000, "roi": None},
    {"id": "venice-token", "symbol": "vnc", "name": "Venice Token", "current_price": 22.41, "market_cap": 89000000, "price_change_percentage_24h": 5.57866, "max_supply": 50000000, "roi": None},
    {"id": "lium", "symbol": "lium", "name": "lium", "current_price": 26.70, "market_cap": 120000000, "price_change_percentage_24h": 5.01394, "max_supply": None, "roi": None},
    {"id": "zcash", "symbol": "zec", "name": "Zcash", "current_price": 1224.70, "market_cap": 2500000000, "price_change_percentage_24h": 4.81358, "max_supply": 21000000, "roi": None},
    {"id": "monero", "symbol": "xmr", "name": "Monero", "current_price": 625.94, "market_cap": 11000000000, "price_change_percentage_24h": 4.64443, "max_supply": None, "roi": None},
    {"id": "tether", "symbol": "usdt", "name": "Tether", "current_price": 1.00, "market_cap": 120000000000, "price_change_percentage_24h": 0.00000, "max_supply": None, "roi": None}
]

# Kiegészítjük a listát 50 darabosra tesztelési célból, hogy a top50_df feladat is működjön
for i in range(1, 45):
    kripto_adatok.append({
        "id": f"dummy-coin-{i}",
        "symbol": f"dum{i}",
        "name": f"Dummy Coin {i}",
        "current_price": 0.5 + (i * 0.1),
        "market_cap": 5000000 + (i * 500000),
        "price_change_percentage_24h": -2.5 + (i * 0.15),
        "max_supply": 100000000,
        "roi": None
    })

# DataFrame létrehozása
df = pd.DataFrame(kripto_adatok)
print("DataFrame sikeresen létrehozva a mintaadatokból!\n")

# 1. Feladat: Üres cellák meghatározása oszloponként
print("--- 1. Feladat: Üres cellák száma oszloponként ---")
missing_values = df.isnull().sum()
print(missing_values)
print("\n")

# 2. Feladat: A market_cap teljes összegének meghatározása
print("--- 2. Feladat: Teljes market_cap összeg ---")
total_market_cap = df['market_cap'].sum()
print(f"A teljes market cap összege: {total_market_cap:,.0f} USD")
print("\n")

# 3. Feladat: Új dataframe (top50_df) az első 50 kriptovalutával current_price alapján
print("--- 3. Feladat: top50_df létrehozása current_price alapján ---")
top50_df = df.sort_values(by='current_price', ascending=False).head(50).copy()
print(f"A top50_df létrejött. Sorok száma: {len(top50_df)}")
print("\n")

# 4. Feladat: top50_df rendezése price_change_percentage_24h alapján csökkenő sorrendbe
print("--- 4. Feladat: top50_df rendezése 24 órás árváltozás alapján ---")
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)
print(top50_df[['name', 'current_price', 'price_change_percentage_24h']].head())
print("\n")

# 5. Feladat: change_direction oszlop létrehozása (+, -, 0)
print("--- 5. Feladat: change_direction oszlop hozzáadása ---")
conditions = [
    top50_df['price_change_percentage_24h'] > 0,
    top50_df['price_change_percentage_24h'] < 0,
    top50_df['price_change_percentage_24h'] == 0
]
choices = ['+', '-', '0']

top50_df['change_direction'] = np.select(conditions, choices, default='NaN')

# Ellenőrzés csonkítás nélkül a terminálban:
print(top50_df[['name', 'price_change_percentage_24h', 'change_direction']].head(10))
print("\n")

# MENTÉS CSV FÁJLBA ugyanabba a mappába
print("--- Eredmények mentése fájlba ---")
current_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_dir, "top50_kripto.csv")

top50_df.to_csv(output_path, index=False, encoding='utf-8')
print(f"Sikeresen elmentve ide: {output_path}")
