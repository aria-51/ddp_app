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

# take song URL
with st.expander('Enter Playlist URL', True):
    playlist_input = st.text_input('Spotify Playlist URL', 'https://open.spotify.com/playlist/1ppIdMJUxRIPXNLP0JxCxJ?si=d02d2bb970a6434b')
    ready_button = st.checkbox('Good to go! Gather Playlist Data')

sp = connect_to_spotify()

if playlist_input and ready_button:
    playlist_details = sp.playlist(playlist_input)

    song_title = playlist_details['name']
    song_artist = playlist_details['owner']['display_name']
    song_image = playlist_details['images'][0]['url']

    col1, col2 = st.columns([60,100])
    with col1:
        st.image(song_image)
        st.subheader(song_title)
        st.write(song_artist)

    # get song titles 
    tracks_total = len(playlist_details['tracks']['items'])
    songs = []
    artists = []
    for i in range(tracks_total):
        songs.append(playlist_details['tracks']['items'][i]['track']['name'])
        artists.append(playlist_details['tracks']['items'][i]['track']['artists'][0]['name'])

    df = pd.DataFrame(columns=['tracks','artist'])
    df['tracks']=songs
    df['artist']=artists

    with col2:
        st.write(df)
    
    # for each song in df calc mood, keep track, do some count, show
    #mood = predict_single_song_mood(song_artist, song_title, train_model(load_data()))
    st.text('The song\'s mood is: '+ 'SPOOKY')
