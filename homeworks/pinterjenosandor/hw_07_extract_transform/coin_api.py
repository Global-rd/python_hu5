import requests
import pandas as pd
import numpy as np


url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250
}
response = requests.get(url, params=parameters)
data = response.json()
df = pd.DataFrame(data)
#print(response.text)#data check what kept

print("->Top 250 Crypto")
print(df[["market_cap_rank" , "name" , "current_price"]]) #list of top 250 crypto


print("->Empty cells by columns:")
print(df.isna().sum()) #check zero columns
#ttl market cap
market_cap_total = (df["market_cap"].sum()) #total market cap
print(f"\n->The total market cap of currencies: {market_cap_total}$\n")

top50_price_df = df.sort_values("current_price", ascending=False).head(50) #top50 crypto price
print(f"->The top 50 currency by price{top50_price_df}")

top50_df_24h_change = top50_price_df.sort_values("price_change_percentage_24h", ascending=False).head(50) #top50change in percentage
print(f"\n->The top 50 currency by 24 change: {top50_df_24h_change}\n")
#transform top 50
#make condition
cond = [
    top50_price_df["price_change_percentage_24h"] > 0,
    top50_price_df["price_change_percentage_24h"] < 0,
    top50_price_df["price_change_percentage_24h"] == 0,
]
change = ["+", "-", "0"] #the list of the characters on same sorted as the conditions
top50_price_df["change_direction"] = np.select(cond, change, default="0") #make the column with numpy
print("->24H change of Top 50 currency:")
print(top50_price_df[["name", "price_change_percentage_24h", "change_direction"]].head(50))