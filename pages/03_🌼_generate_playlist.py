import streamlit as st
from helper_funct import add_logo, setup_page, connect_to_spotify, train_model, predict_single_song_mood, connect_to_spotify, extra_auth
import pandas as pd
import re
import streamlit.components.v1 as components


setup_page()
add_logo()
sp = connect_to_spotify()

user_input = st.text_input('Enter your vibe here:', 'jump around your room')
ready_button = st.checkbox('Generate my playlist')

if ready_button:

    # predict the vibes of the text here
    prediction = 'happy'

    # get 10 songs from our playlist
    # get csv into df
    df = pd.read_csv('pages/song_repo.csv')
    #st.write(df[df.mood.eq(prediction)].sample(2))

    # fake seed songs
    artists = ['One Republic', 'The Hunna']
    song_titles = ['Sunshine','I Wanna Know']

    # Get details of seed songs
    artists_uri = []
    songs_uri = []
    artists_genres = set()

    for i in range(len(song_titles)):
        query = artists[i]+' '+song_titles[i]

        result = sp.search(query)

        regex ='(?:spotify:track:|spotify:artist:)([a-zA-Z0-9]+).*'
        track_uri = re.findall(regex, result['tracks']['items'][0]['uri'])[0]
        artist_uri = re.findall(regex, result['tracks']['items'][0]['artists'][0]['uri'])[0]
        artist_genres = sp.artist(artist_uri)['genres']

        artists_uri.append(artist_uri)
        songs_uri.append(track_uri)
        artists_genres.update(artist_genres)

    # allow ppl to pick genre from list
    available_genres = sp.recommendation_genre_seeds()['genres']
    ok_options = set(artists_genres) & set(available_genres)

    options = st.multiselect('Select preferred genres for playlist (max 2)', ok_options, ['rock'], max_selections = 2)
    # only 4 in total :) thanks spotify
    title_input = st.text_input('Give a name to your playlist','how exciting')

    if st.button('Ready!'):
        # extend with spotify
        # get recomm tracks
        recom_gen = sp.recommendations(seed_tracks=songs_uri, seed_genres=options)#, seed_artists=artists_uri)
        tracks_uri=[]
        for item in recom_gen['tracks']:
            tracks_uri.append(re.findall(regex, item['uri'])[0])

        # create playlist & add tracks
        sp = extra_auth()
        playlist = sp.user_playlist_create('rayna747', name= title_input)
        playlist_id = playlist["id"]
        sp.playlist_add_items(playlist_id, tracks_uri)

        # show playlist on page
        uri_link = 'https://open.spotify.com/embed/playlist/' + playlist_id
        components.iframe(uri_link, height= 400)
        
