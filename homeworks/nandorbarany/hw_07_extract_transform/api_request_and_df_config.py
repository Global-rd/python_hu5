import requests
import pandas as pd
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url=url, params=parameters).json()

df = pd.DataFrame(response)

print(df.iloc[0:5, 0:10]) # checking df layout

# empty_cells/column
empty_cells_per_column = df.isna().sum()
print(f"Empty cells per column:\n{empty_cells_per_column}")

# total market_cap
total_market_cap = df['market_cap'].sum()
print(f"Total market_cap: ${total_market_cap}")

# top50_df
top50_df = df.sort_values("current_price", ascending=False).head(50)

# top sorted by pricechange
top50_df_price_change = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(f"Top 50 crypto by price change:\n{top50_df_price_change[['name', 'current_price', 'price_change_percentage_24h']]}")

# change_direction column
def new_column(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

vectorized = np.vectorize(new_column)
top50_df["change_direction"] = vectorized(top50_df["price_change_percentage_24h"])

print(f"Top 50 crypto with change direction column:\n{top50_df[['name', 'current_price', 'price_change_percentage_24h', 'change_direction']]}")