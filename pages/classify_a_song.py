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

data_file = 'pages/song_lyrics.csv'

@st.cache
def load_data():
    data = pd.read_csv(data_file)
    data =  data.drop(columns='song_id')
    return data

model = train_model(load_data())

# take song URL
with st.expander('Enter Song URL', True):
    song_input = st.text_input('Spotify Song ID', 'https://open.spotify.com/track/7azo4rpSUh8nXgtonC6Pkq?si=c64586a6fa1d443c')
    ready_button = st.checkbox('Good to go! Gather Song Data')

sp = connect_to_spotify()

# if there is an entry in the song part and the button is clicked # can this be an actual button?
if song_input and ready_button:

    song_details = sp.track(song_input)

    song_title = song_details['name']
    song_artist = song_details['artists'][0]['name']
    song_image = song_details['album']['images'][1]['url']

    col1, col2, col3 = st.columns([60,50,50])
    with col1:
        st.image(song_image)
    with col2:
        st.text(song_artist)
    with col3:
        st.text(song_title)
    
    mood = predict_single_song_mood(song_artist, song_title, model)
    st.text('The song\'s mood is: '+ mood)