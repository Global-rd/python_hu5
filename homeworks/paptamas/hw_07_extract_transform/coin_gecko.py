import requests
import pandas as pd

# API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# Request parameters
params = {
    "vs_currency": "usd",
    "per_page": 250
}

# Send request to CoinGecko API
response = requests.get(url, params=params)

# Raise an exception if the request failed
response.raise_for_status()

# Convert JSON response to DataFrame
df = pd.DataFrame(response.json())

# 1. Count missing values in each column
print("Missing values per column:")
print(df.isnull().sum())

# 2. Calculate total market capitalization
total_market_cap = df["market_cap"].sum()

print("\nTotal market cap:")
print(total_market_cap)

# 3. Create a new DataFrame containing the top 50 cryptocurrencies
# based on current price
top50_df = (
    df.sort_values(by="current_price", ascending=False)
      .head(50)
      .copy()
)

# 4. Sort the DataFrame by 24-hour price change percentage
# in descending order
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

# 5. Create a new column called change_direction
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

# Display results
print("\nTop 50 cryptocurrencies:")
print(
    top50_df[
        [
            "name",
            "current_price",
            "price_change_percentage_24h",
            "change_direction"
        ]
    ]
)