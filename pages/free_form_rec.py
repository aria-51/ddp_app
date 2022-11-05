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
