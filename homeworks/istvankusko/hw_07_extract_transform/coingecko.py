# api

import os
import pandas as pd
import requests

# 0. Create directory (replace 'your_name' with your actual name or path)
base_dir = "your_name"
target_dir = os.path.join(base_dir, "hw_07_extract_transform")
os.makedirs(target_dir, exist_ok=True)

# 1. Fetch data from the CoinGecko API (Top 250 coins by market cap)
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
}

response = requests.get(url, params=params)
data = response.json()

# Create DataFrame
df = pd.DataFrame(data)

print("--- 1. Number of empty cells per column ---")
null_counts = df.isnull().sum()
print(null_counts)
print("\n" + "=" * 50 + "\n")

print("--- 2. Total sum of market_cap ---")
total_market_cap = df["market_cap"].sum()
print(f"Total market cap of the 250 cryptocurrencies: {total_market_cap:,.2f} USD")
print("\n" + "=" * 50 + "\n")

# 3. Create top50_df based on current_price (highest price first)
top50_df = df.sort_values(by="current_price", ascending=False).head(50).copy()

# 4. Sort top50_df by price_change_percentage_24h in descending order
top50_df.sort_values(
    by="price_change_percentage_24h", ascending=False, inplace=True
)

# 5. Create a new column 'change_direction' (+, -, 0)
def get_direction(val):
    if pd.isna(val):
        return None
    elif val > 0:
        return "+"
    elif val < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    get_direction
)

print("--- 3-5. Results (First 10 rows of top50_df) ---")
print(
    top50_df[
        ["name", "symbol", "current_price", "price_change_percentage_24h", "change_direction"]
    ].head(10)
)

# Optional: Save top50_df to CSV inside the target folder
output_file = os.path.join(target_dir, "crypto_top50_analysis.csv")
top50_df.to_csv(output_file, index=False)
print(f"\ntop50_df successfully saved to: {output_file}")