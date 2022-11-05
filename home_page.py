import streamlit as st
from helper_funct import add_logo, get_random_artwork
from PIL import Image

st.set_page_config(
                    page_title='DDP Demo',
                    page_icon=Image.open('cats.jpg'),
                    layout='wide'
                    )

add_logo()

st.image(get_random_artwork(10), width=100)
st.markdown("<h1 style='text-align: center;'>Welcome to MoodClass</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>A new way to discover music...</h2>", unsafe_allow_html=True)
st.image(get_random_artwork(30), width=100)