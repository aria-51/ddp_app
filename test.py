from helper_funct import connect_to_spotify
import re

artists = ['One Republic', 'The Hunna']
song_titles = ['Sunshine','I Wanna Know']

sp = connect_to_spotify()
artists_uri = []
songs_uri = []
artists_genres = []

for i in range(len(song_titles)):
    query = artists[i]+' '+song_titles[i]
    print(query)

    result = sp.search(query)

    regex ='(?:spotify:track:|spotify:artist:)([a-zA-Z0-9]+).*'
    track_uri = re.findall(regex, result['tracks']['items'][0]['uri'])[0]
    artist_uri = re.findall(regex, result['tracks']['items'][0]['artists'][0]['uri'])[0]
    artist_genres = sp.artist(artist_uri)['genres']

    artists_uri.append(artist_uri)
    songs_uri.append(track_uri)
    artists_genres.extend(artist_genres)

print(songs_uri, artists_uri, artists_genres)