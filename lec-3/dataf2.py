import requests, zipfile
from io import StringIO
import io
import pandas as pd

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

print(anime_data.head())
print(anime_data.info())
print(anime_data.describe())

col_use=['MAL_ID', 'Name', 'Type', 'Episodes', 'Members', 'Score']
anime_data = anime_data[col_use]
print(anime_data.head())
print(anime_data[0:3])