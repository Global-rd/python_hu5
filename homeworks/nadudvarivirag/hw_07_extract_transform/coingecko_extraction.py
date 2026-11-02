#https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&x_cg_demo_api_key=CG-y1MjLKWyoGXoLJZumZhFa1BD

import pandas as pd
import numpy as np
import requests
import settings as s
import pandas as pd
import time
import os


url = "https://api.coingecko.com/api/v3/coins/markets"


    
parameters = {"vs_currency": "usd",
          "order": "market_cap_desc",
          "per_page": "250",
          "page" : 1,
          "sparkline": "False",
          "x_cg_demo_api_key": s.COINGECO_API_KEY}

response = requests.get(url=url, params=parameters).json()

#print(response)
df = pd.DataFrame(response)
#print(df[["name"],["market_cap"]])
#print(df)

# 1. üres cellák meghatározása oszloponként
count_na = df.isna().sum()
print(count_na)

# 2. market_cap összege az egész data framre
sum_market_cap = df["market_cap"].sum()
print(sum_market_cap)

# 3. első 50 kriptovaluta current_price alapján
top_50_df = df.nlargest(50, "current_price")
print(top_50_df)

# 4. top50_df price_change_percentage_24h alapján csökkenő sorrendbe
top_50_df= top_50_df.sort_values(by="price_change_percentage_24h", 
                                 ascending=False)
print(top_50_df[["name", "current_price", "price_change_percentage_24h"]])

# 5. change direction
def categorize_change_direction (price_change_percentage_24h):
    if price_change_percentage_24h > 0:
        return "+"
    elif price_change_percentage_24h < 0:
        return "-"
    else:
        return "0"
categorize_change_direction_vectorized = np.vectorize(categorize_change_direction)

    
top_50_df["categorize_change_direction"] = categorize_change_direction_vectorized(top_50_df["price_change_percentage_24h"])
print(top_50_df)