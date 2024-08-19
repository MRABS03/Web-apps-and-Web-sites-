import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')

st.title('The Best Company')
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor
 incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
 laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse
  cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa
   qui officia deserunt mollit anim id est laborum""")

st.header('Our Team')
col1,col2,col3=st.columns(3)

df=pd.read_csv('datacomp.csv')

with col1:
    for index,row in df[:4].iterrows():
        st.header(fr"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(fr"Images\{row['image']}")

with col2:
    for index,row in df[4:8].iterrows():
        st.header(fr"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(fr"Images\{row['image']}")

with col3:
    for index,row in df[8:].iterrows():
        st.header(fr"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(fr"Images\{row['image']}")
