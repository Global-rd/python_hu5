import streamlit as st

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.markdown("Markdown")
st.caption("Caption")

code_example = """
def greet(name):
    print(f"Hello {name}")
"""
st.code(code_example, language="python")

st.divider()