import pandas as pd
import numpy as np
from extract_coingecko import extract_data

#Creating dataframe (df) from data from API
df = pd.DataFrame(extract_data())

#Checking if df is alright, getting basic df info
print("The dataframe & info:")
print(df)
print("\n")

df.info()
print("\n")

# 1. Printing number of empty cells per column
print("Empty cell counts per column:")
print(df.shape[0] - df.count())

# 2. Printing the total market capital value of df
print(f"\nMarket capital total: {df["market_cap"].sum():,}".replace(',', ' '))
print("\n")

# 3. Creating and printig a new df (top50_df) - the 50 first record by price, reseting the index of the new df
top50_df = df.sort_values(by="current_price", ascending=False).head(50).reset_index(drop=True)
print("Top 50 record in descending order by price:")
print(top50_df)
print("\n")

# 4. Sorting the top50_df by price change percentage over the last 24 hrs in descending order
top50_df.sort_values(by="price_change_percentage_24h", ascending=False, inplace=True)
print("Top 50 record in descending order by price change percentage over the last 24 hrs:")
print(top50_df)
print("\n")

# 5. Adding a new column (change direction) to top50_df showing the direction of price change percentage over the last 24
top50_df["change_direction"] = np.select(
    [top50_df["price_change_percentage_24h"] > 0,
    top50_df["price_change_percentage_24h"] < 0],
    ["+", "-"],
    default="0")
print("First fiverows of the top 50 record with newly added 'change_direction' column:")
print(top50_df.head())