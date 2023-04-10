import pandas as pd;
from nltk.corpus import stopwords
import re

import nltk
from nltk.stem import PorterStemmer 
ps = PorterStemmer()
stop_words = stopwords.words('english')

df = pd.read_csv('./data/lyrics-data.csv')
df_artists = pd.read_csv('./data/artists-data.csv')
df = df[df.language == 'en']
df = df.join(df_artists.set_index('Link'), on='ALink')
df = df.drop(columns=['ALink','Songs', 'SLink', 'language', 'Popularity'])

print(df.columns)

remove = ['verse 1', 'verse 1']
def clean_lyrics(string):
    string = string.lower()
    string.replace('chorus','')
    string = re.sub(r'[^\w]', ' ', string)
    return string

print(df['Lyric'].iat[0])
df['Lyric'] = df['Lyric'].apply(lambda x: clean_lyrics(x))
df.to_csv('./data/cleaned_songs.csv')