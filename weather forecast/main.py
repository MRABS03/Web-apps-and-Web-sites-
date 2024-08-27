import streamlit as st
import plotly.express as px
from backend import retrieve_data

st.set_page_config(page_title="Weather",layout='centered')
st.title("Future weather forecast!!")
st.header("Place")
location=st.text_input("Enter the city name!")
days=st.slider(min_value=1,max_value=5,label="Forecast days!")
mode_list=['Temperature','Sky']

mode=st.selectbox("What mode do you want to select: ",mode_list)
if int(days)==1:
    st.header(fr"{mode} for next {days} day in {location}")
elif int(days)>1:
    st.header(fr"{mode} for next {days} days in {location}")

if location:
    try:
        data, dates = retrieve_data(location=location, days=days, mode=mode)

        if mode == "Temperature":
            figure = px.line(x=dates, y=data, labels={'x': "Date", 'y': "Temperature (°C)"})
            st.plotly_chart(figure)

        elif mode == 'Sky':
            sky_conditions = [f"images/{condition}.png" for condition in data]
            st.image(sky_conditions, width=115, caption=dates)

    except KeyError:
        st.text(
            f"Please enter a valid city name .")
