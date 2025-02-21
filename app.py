import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Car Sales Analysis")

df = pd.read_csv("vehicles_us.csv")
#st.plotly_chart(px.histogram())

if st.checkbox("Show only cars under $20,000"):
    df = df[df['price'] < 20000]

st.write(df.head())

#st.plotly_chart(#plot command you used in EDA.ipynb)