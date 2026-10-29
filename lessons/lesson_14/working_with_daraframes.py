import pandas as pd
import numpy as np

df = pd.read_csv("lessons/lesson_14/datasets/supermarket_sales.csv", dtype={"Invoice ID": "string"})
print(df)
print(df.dtypes)
print(df.info())
print(df.describe())

print(df.head(10))
print(df.tail())

product_price_df = df[["Product line", "Unit price"]]
print(product_price_df)
print(type(product_price_df))

#LOC
print("-------------")

print(df.loc[1, "Product line"])
print(df.loc[1:3, ['Product line', 'Unit price']])

#.iloc
print("------------")
print(df.iloc[1,1])
print(df.iloc[1:3, [1,2]])



#aggragation and grouping

print("------------------")

#total sales per city and product line
total_sales_df = df.groupby(['City', 'Product line'])['Total'].sum().reset_index().sort_values(['City','Total'], ascending=False)
print(total_sales_df)

avg_rating_df = df.groupby(['Customer type', 'Payment'])['Rating'].mean().reset_index()

print(avg_rating_df)

print("-------filtering------")

yangon_df = df[df["City"] == "Yangon"] 
print(yangon_df)

print(yangon_df["City"].unique())


#method chaining

result_df = (df[df['City']=="Yangon"]
             .groupby('Gender')
             .agg({'Unit price': 'mean'})
             .reset_index()
             .sort_values('Unit price', ascending=False))

print(result_df)


print("------------------")

df_stock_base = pd.read_csv("lessons/lesson_14/datasets/stock_base.csv")
df_stock_extension = pd.read_csv("lessons/lesson_14/datasets/stock_extension.csv")

print(df_stock_base)
print(df_stock_extension)

merged_df = pd.merge(left=df_stock_base,
                     right=df_stock_extension,
                     on="id",
                     how="inner",
                     validate="1:1")

print(merged_df)


def categorize_stock(price):
    if price > 1000:
        return "Premium"
    else:
        return "Standard"


categorized_stock_vectorized = np.vectorize(categorize_stock)
merged_df["category"] = categorized_stock_vectorized(merged_df["price"])



merged_df["category"] = np.where(merged_df["price"] > 1000, "Premium", "Standard")

print(merged_df)

