"""Minimal Streamlit demo."""
import pandas as pd
import streamlit as st

st.title("project-management-analytics-portfolio")
df = pd.read_csv("data/resource_utilization.csv")
st.dataframe(df.head(20))
