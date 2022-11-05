import streamlit as st
import pandas as pd 
import numpy as np

# add title
st.title('the coolest DDP project ever')

with st.sidebar:
    st.markdown("## the")
    st.title('the coolest ddp project')


data_file = 'song_lyrics.csv'

@st.cache
def load_data():
    data = pd.read_csv(data_file)
    data =  data.drop(columns='song_id')
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state = st.text('Done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Building the model (need to be outside)
X = data.drop(columns=['mood'])
y = data['mood']

# create model features count vect, target mood
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB().fit(X.values, y)

# Get input from user
st.subheader('Write the mood you want here')
user_input = st.text_input("Write the mood you want")

'''import streamlit.components.v1 as components
playlist_uri = '37i9dQZF1DX0kbJZpiYdZl'
uri_link = 'https://open.spotify.com/embed/playlist/' + playlist_uri
components.iframe(uri_link, height=300)'''

# beach party
user_input_transf = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 1]]


mood = 'n/a'

pred = model.predict(user_input_transf)

if pred==1:
    mood = 'romantic'
elif pred==2:
    mood = 'happy'
else:
    mood = 'undetermined'

st.text('The mood reflective for your words is: '+ mood)



'''
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
'''