import streamlit as st
from helper_funct import add_logo, setup_page, get_playlist_mood, connect_to_spotify
import pandas as pd
import streamlit.components.v1 as components
import re

setup_page()
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
        #st.write(song_artist)

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
        match_re = 'playlist[\/:](.+)[\s?]'
        playlist_uri = re.findall(match_re, playlist_input)[0]
        uri_link = 'https://open.spotify.com/embed/playlist/' + playlist_uri
        components.iframe(uri_link, height= 400)
    
    # for each song in df calc mood, keep track, do some count, show
    pred = get_playlist_mood(df)
    st.text('The playlist\'s mood is: ' + pred)