import pandas as pd
import streamlit
import streamlit as st
import plotly.express as ps

st.set_page_config(page_title="Happiness stats", layout='centered')
df = pd.read_csv("happy.csv")

streamlit.title("In Search for Happiness")
cols = list(df.columns)
st.subheader("Select the data for X-axis")
x_axis = st.selectbox("X-axis data..", cols)
st.subheader("Select the data for Y-axis")
cols.remove(x_axis)
y_axis = st.selectbox("Y-axis data..", cols)

st.header(fr"{x_axis} and {y_axis}")


def get_data(x_axis, y_axis):
    x_axis_data = list(df[f'{x_axis}'])
    y_axis_data = list(df[f'{y_axis}'])
    return x_axis_data, y_axis_data


x, y = get_data(x_axis, y_axis)
figure=ps.scatter(x=x,y=y,labels={'x': f"{x_axis}" ,'y':f"{y_axis}"})
st.plotly_chart(figure)