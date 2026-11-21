import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

missing_values = df.isna().sum()

print("Empty cells in each column:")
print(missing_values)

total_market_cap = df["market_cap"].sum()

print("Total market cap:")
print(total_market_cap)


top50_df = df.sort_values(
    by="current_price",
    ascending=False
).head(50)

top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

def get_change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    elif value == 0:
        return "0"

    return None

top50_df["change_direction"] = top50_df[
    "price_change_percentage_24h"
].apply(get_change_direction)
