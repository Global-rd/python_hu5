import pandas as pd

#creating dataframes
#from 2 or more series

s1 = pd.Series([1,2,3], index=["a", "b", "c"])
s2 = pd.Series([4,5,6], index=["a", "b", "c"])

df = pd.DataFrame({"col1": s1, "col2": s2})
print(df)
print(type(df))

s1 = pd.Series([1,2,3], index=["a", "b", "c"])
s2 = pd.Series([4,5,6], index=["b", "c", "d"])

df = pd.DataFrame({"col1": s1, "col2": s2})
print(df)
print(type(df))

df = df.fillna(0)
print(df)


#python structures

data = {"ID": [1,2,3],
        "Name": ['Alice', 'Timmy', 'Jimmy'],
        "Age": [12, 25, 35]}

df = pd.DataFrame(data)
print(df)

data = [
    {"ID": 1, "Name": "Alice", 'Age': 13},
    {"ID": 1, "Name": "Alice", 'Age': 13},
    {"ID": 1, "Name": "Alice", 'Age': 13}
]

df = pd.DataFrame(data)
print(df)


data = [
    [1, 'Alice', 13],
    [1, 'Alice', 13],
    [1, 'Alice', 13]
]

df = pd.DataFrame(data, columns=["ID", "Name", "Age"])
print(df)


#create dataframe from files
supermarket_df = pd.read_csv("lessons/lesson_14/datasets/supermarket_sales.csv")
print(supermarket_df)

df = pd.read_json("lessons/lesson_14/datasets/test.json")
print(df)


#convert back to python structure

data_as_list_of_dicts = df.to_dict(orient="records")
print(data_as_list_of_dicts)
data_as_dict_of_lists = df.to_dict(orient="list")
print(data_as_dict_of_lists)
data_as_list_of_lists = df.values.tolist()
print(data_as_list_of_lists)

df.to_csv("lessons/lesson_14/datasets/test.csv", index=False)
