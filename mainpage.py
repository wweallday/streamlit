import streamlit as st
import time 
import numpy as np
import webbrowser

st.set_page_config(page_title="first page")

st.sidebar.header("this is a side bar")
st.write(
  "Hello world! dcm"
)
url = 'https://youtu.be/dQw4w9WgXcQ'

if st.button('Open browser'):
    webbrowser.open_new_tab(url)