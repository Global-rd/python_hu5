import pandas as pd
import requests


url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    
"vs_currency": "usd",
"per_page": 250
}

response_df = pd.DataFrame(requests.get(url=url, params=params).json())

print(response_df)
# 1. feladat
isna_response_df = response_df.isna().sum()
print(isna_response_df)

# 2. feladat

market_cap_sum = response_df["market_cap"].sum()
print(market_cap_sum)

# 3. feladat

first_50_current = response_df.sort_values(by="current_price", ascending=False).head(50)
print(first_50_current)

# 4. feladat

first_50 = first_50_current.sort_values(by="price_change_percentage_24h", ascending=False)

# 5. feladat

def change_direction (change):
    if  change  > 0:
        return "+"
    if  change < 0:
        return "-"
    if  change == 0:
        return "0"

first_50["change_direction"] = first_50["price_change_percentage_24h"].apply(change_direction)



