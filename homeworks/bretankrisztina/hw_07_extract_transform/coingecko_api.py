import requests
import pandas as pd
import numpy as np

#API endpoint for CoinGecko to get market data for coins
url = "https://api.coingecko.com/api/v3/coins/markets"

#Request parameters for the API call, including the currency and number of results per page
params = {
    "vs_currency": "usd",
    "per_page": 250
}

#Make the API call to CoinGecko and store the response in a variable
response = requests.get(url=url, params=params, timeout=30)
response.raise_for_status()

#Create a DataFrame from the response data
df = pd.DataFrame(response.json())

#Print the first 5 rows of the DataFrame to the console
print(df.head())

#calculating the number of missing values in each column
print("Missing values per column are:", df.isnull().sum())

#Determine the amount of market_cap
print("The amount of market_cap is:", df["market_cap"].sum())

#Creating a new dataframe- name top50_df by current_price - largest 50 coins
top50_df = df.sort_values(
    by="current_price",
    ascending=False
).head(50).reset_index(drop= True)

print(top50_df[["name", "current_price"]])

#Sorting the top50_df by price_change_percentage_24h in descending order
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
).reset_index(drop=True)

print(top50_df[["name", "current_price", "price_change_percentage_24h"]])

#Creating a new column to the top50_df called "change direction" based on the price_change_percentage_24h column
def change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"
    
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])

change_direction_vectorized = np.vectorize(change_direction)
top50_df["change_direction"] = change_direction_vectorized(top50_df["price_change_percentage_24h"])
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])