import streamlit as st
from helper_funct import add_logo, train_model, predict_single_song_mood, connect_to_spotify
from PIL import Image
import pandas as pd

st.set_page_config(
                    page_title='DDP Demo',
                    page_icon=Image.open('cats.jpg'),
                    layout='wide'
                    )

add_logo()

user_input = st.text_input('Enter your vibe here:','beach party')

if st.button('Generate my playlist!'):
    st.audio('https://p.scdn.co/mp3-preview/135c5c2caba0db75f946dec7e93fdb752fe8d399?cid=db90a7924baf4b38a9cbb37964f71044')

    # predict the vibes of the text here

    # get 10 songs from our playlist

    # extend with spotify