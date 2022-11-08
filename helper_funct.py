import streamlit as st
import glob, random
from lyrics_function import get_lyrics
from PIL import Image

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

def train_model(df):
    X = df.drop(columns=['mood'])
    y = df['mood']

    # create model features count vect, target mood
    from sklearn.naive_bayes import MultinomialNB
    trained_model = MultinomialNB().fit(X.values, y)

    return trained_model

def vectorize():
    pass

def predict_single_song_mood(title, artist, model):
    # get artist

    # get title

    # get lyrics
    lyrics = get_lyrics(artist, title)

    # transform lyrics
    # beach party
    user_input_transf = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 1]]

    # predict
    pred = model.predict(user_input_transf)

    # transform pred into name
    if pred==1:
        mood = 'romantic'
    elif pred==2:
        mood = 'happy'
    else:
        mood = 'undetermined'

    return mood

def connect_to_spotify():
    # connect to spotify
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    auth_manager = SpotifyClientCredentials(client_id='db90a7924baf4b38a9cbb37964f71044', client_secret = '27599d5076e74b29b99d0f3e0f1caa92')
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp