import streamlit as st
import requests

api_key = "xA7X8UyNMuo2i9hT5Ho4Fegfiaw5wjIIlGh2twLC"
url = "https://api.nasa.gov/planetary/apod"

params={
    'api_key':api_key
}

request = requests.get(url,params=params)
content=request.json()
print(content)

st.set_page_config(layout='centered')
Title=content['title'].title()
image_url=content['hdurl']
description=content["explanation"]

st.title(Title)
st.image(image_url)
st.write(description)

