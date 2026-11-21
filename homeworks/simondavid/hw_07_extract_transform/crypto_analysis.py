import requests
import pandas as pd

# Fetch cryptocurrency data from CoinGecko
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

print(f"Retrieved {len(data)} cryptocurrencies.")

# Create DataFrame
df = pd.DataFrame(data)

# 1. Check missing values in all columns
print("\nMissing values:")
print(df.isnull().sum())

# 2. Calculate total market cap
total_market_cap = df["market_cap"].sum()

print(f"\nTotal market cap: ${total_market_cap:,.2f}")

# Convert USD prices to EUR
usd_to_eur = 0.92

df["price_eur"] = df["current_price"] * usd_to_eur

print("\nPrices in USD and EUR:")
print(df[["name", "current_price", "price_eur"]].head(10))

# 3. Create a DataFrame with the 50 most expensive cryptocurrencies
top50_df = df.sort_values(
    by="current_price",
    ascending=False
).head(50).copy()

print("\nTop 50 cryptocurrencies by price:")
print(top50_df[["name", "symbol", "current_price"]])

# 4. Sort Top 50 by 24-hour price change (descending)
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

print("\nTop 50 sorted by 24-hour price change:")
print(top50_df[["name", "symbol", "price_change_percentage_24h"]])

# 5. Create change_direction column
def get_change_direction(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"


top50_df["change_direction"] = top50_df[
    "price_change_percentage_24h"
].apply(get_change_direction)

print("\nTop 50 with change direction:")
print(top50_df[
    ["name", "symbol", "price_change_percentage_24h", "change_direction"]
])

# Extra: Top 10 gainers in the last 24 hours
top_gainers = df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
).head(10)

print("\nTop 10 gainers in the last 24 hours:")
print(top_gainers[
    ["name", "symbol", "price_change_percentage_24h"]
])