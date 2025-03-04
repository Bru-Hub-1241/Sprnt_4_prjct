from numpy import size
import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Car Sales Analysis")

df = pd.read_csv("vehicles_us.csv")
#st.plotly_chart(px.histogram())

if st.checkbox("Show only cars under $20,000"):
    df = df[df['price'] < 20000]

st.write(df.head())

st.plotly_chart(px.histogram(df, x='price', nbins=50, title='car prices'))


fig = px.scatter(df, x='price', y='model_year',)
st.plotly_chart(fig)

fig = px.scatter(df, x='model', y='model_year', color= 'paint_color', title= 'Vehicle Model Scatter Plot') 
st.plotly_chart(fig)

st.plotly_chart(px.histogram(df, x='odometer', nbins=40, title='milage amount'))

print(df[df['type'] == df['type'].max()])