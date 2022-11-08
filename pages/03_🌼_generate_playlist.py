import streamlit as st
from helper_funct import add_logo, setup_page, train_model, predict_single_song_mood, connect_to_spotify

setup_page()
add_logo()

user_input = st.text_input('Enter your vibe here:','beach party')

if st.button('Generate my playlist!'):
    st.audio('https://p.scdn.co/mp3-preview/135c5c2caba0db75f946dec7e93fdb752fe8d399?cid=db90a7924baf4b38a9cbb37964f71044')

    # predict the vibes of the text here

    # get 10 songs from our playlist

    # extend with spotify