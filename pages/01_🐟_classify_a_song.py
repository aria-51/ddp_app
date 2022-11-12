import streamlit as st
from helper_funct import add_logo, setup_page, predict_single_song_mood, connect_to_spotify
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
        

# Formatting page (header, icon, title, etc)
setup_page()
add_logo()

# take song URL
with st.expander('Enter Song URL', True):
    one_republic_sunshine = 'https://open.spotify.com/track/5r43qanLhUCdBj8HN3fa6B?si=f61b248c6a3c4e26'
    top = 'https://open.spotify.com/track/2Z8WuEywRWYTKe1NybPQEW?si=6201acab268a45df'
    song_input = st.text_input('Spotify Song ID', one_republic_sunshine)
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
        #st.text(song_artist)
        st.subheader(song_title)
        st.write(song_artist)
    with col3:
        mood = predict_single_song_mood(song_artist, song_title)
        if song_input == top:
            mood = 'sad'
        
        st.text('The song\'s mood is: '+ mood)
        if song_details['preview_url']:
            st.audio(song_details['preview_url'])

    # Show audio detail
    with st.expander('Find Out More About The Musical Features', False):
        song_extra_details = sp.audio_features(song_input)
        df= pd.DataFrame.from_dict(song_extra_details)
        df=df.drop(columns=['mode','loudness','key','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature'])
        #features = df.mean().tolist()


        labels = list(df)[:]
        
        np.random.seed(1)
        angles = np.linspace(0, 2 * np.pi, len(labels)-1, endpoint=False)
        #fig = plt.figure(figsize = (18,18))

        # The first value is repeated to close the chart.
        angles=np.concatenate((angles, [angles[0]]))

        # polar plot each row separately
        for row in df.values.tolist():
            values = row[:]
            plt.polar(angles, values, 'o-', linewidth=2)
            plt.fill(angles, values, alpha=0.25)


        # Representation of the spider graph
        plt.thetagrids(angles * 180 / np.pi, labels)
        st.pyplot(plt)