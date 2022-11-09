import streamlit as st
from helper_funct import add_logo, setup_page, predict_single_song_mood, connect_to_spotify
import pandas as pd

# Formatting page (header, icon, title, etc)
setup_page()
add_logo()

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
    
    #st.audio('https://p.scdn.co/mp3-preview/135c5c2caba0db75f946dec7e93fdb752fe8d399?cid=db90a7924baf4b38a9cbb37964f71044')

    col1, col2, col3 = st.columns([60,50,50])
    with col1:
        st.image(song_image)
        st.audio(song_details['preview_url'])
    with col2:
        st.text(song_artist)
    with col3:
        st.text(song_title)
    
    mood = predict_single_song_mood(song_artist, song_title)
    st.text('The song\'s mood is: '+ mood)

    # Show audio detail
    with st.expander('Find Out More About The Musical Features', False):
        song_extra_details = sp.audio_features(song_input)
        df= pd.DataFrame.from_dict(song_extra_details)
        df=df.drop(columns=['mode','loudness','key','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature'])
        #features = df.mean().tolist()

        import matplotlib.pyplot as plt
        import numpy as np
        
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