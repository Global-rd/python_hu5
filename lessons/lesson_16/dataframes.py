import streamlit as st
import pandas as pd

st.title("Read only supermarket data")
supermarket_df = pd.read_csv("lessons/lesson_16/test_data/supermarket_sales.csv")
st.dataframe(supermarket_df)

st.title("Editable dataframe")
editable_df = st.data_editor(supermarket_df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
