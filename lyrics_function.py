from lyricsgenius import Genius
import re
import nltk 
from nltk import pos_tag
#nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

client_id = 'BMU2d7PVnIvEnVFKQiMlwJFcSffuHq2epuHYfqTstC7CiqLqSC42KMDTEVTPnRsY'
client_secret ='6Sh1I8isQGva9bIDg8qDnCSEnHbfQy71SurcywPLj2s8R9S1W8MdpprpYdqSPR2AO8c79njZlhSl9RHnxB_5vw'
token = 'sL8fGLHNCUnND1eoeMd6t3-gLWvSet8sU-zoBfauaIPuOXlbKuZrdX2hJiXGFWjD'

def get_lyrics(artist, song_title):

    genius = Genius(token)
    genius.remove_section_headers = True

    try:
        lyrics = genius.search_song(song_title, artist).lyrics
    except:
        lyrics=''

    lyrics = clean_lyrics(lyrics)

    return lyrics

#Mapping POS tag to first character lemmatize() accepts
def get_wordnet_pos(word):
        
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

#Function to Lemmatize every word and remove stopwords 
def lemma(text):
    
    # Setting stopwords
    stop = set(stopwords.words("english"))

    #Initializing Lemmatizer
    lemmatizer = WordNetLemmatizer()

    text = [lemmatizer.lemmatize(x, get_wordnet_pos(x)) for x in nltk.word_tokenize(text)]
    text = [x for x in text if x not in stop]
    return ' '.join(text)

def clean_lyrics(lyrics):

    lyrics = " ".join(re.findall("[a-zA-Z]+", lyrics))
    lyrics = lyrics.lower()

    lyrics = lemma(lyrics)

    return lyrics