import streamlit as st
import glob, random
from lyrics_function import get_lyrics
from PIL import Image
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from model_funct import get_trained_model, get_trained_vectorizer

def setup_page():
    st.set_page_config(
                    page_title='ddp demo | any questions?',
                    page_icon=Image.open('any_questions.jpg'),
                    layout='wide'
                    )

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "your guide, bob";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def get_random_artwork(n):
    file_path_type = ["./album_covers/*.jpg"]
    images = glob.glob(random.choice(file_path_type))
    image_list =[]
    for i in range(n):
        image_list.append(random.choice(images))
    return image_list

def predict_single_song_mood(artist, title):
    # get lyrics
    lyrics = get_lyrics(artist, title)

    # transform lyrics
    vectorzier = get_trained_vectorizer()
    user_input_transf = vectorzier.transform([lyrics])

    # predict
    model = get_trained_model()
    pred = model.predict(user_input_transf)

    return pred[0]

def get_playlist_mood(df):
    predictions = []
    for index, row in df.iterrows():
        song_pred = predict_single_song_mood(row['artist'],row['tracks'])
        predictions.append(song_pred)
    
    most_freq = max(set(predictions), key = predictions.count)
    
    return most_freq

def connect_to_spotify():
    auth_manager = SpotifyClientCredentials(client_id='86f1cd94b44f45788a5f11660f8d3c25', client_secret = 'def8194bba264a5a871170bac6fca086')
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def extra_auth():

    client_id = '86f1cd94b44f45788a5f11660f8d3c25'
    client_secret = 'def8194bba264a5a871170bac6fca086'
    redirect_uri = 'http://localhost:8888/callback/'
    username = 'rayna747'
    scope = 'playlist-modify-public'

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) 
    sp = spotipy.Spotify(token)
    
    return sp