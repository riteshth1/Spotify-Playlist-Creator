from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Taking user input
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"

# Spotify app credentials
CLIENT_ID = "b572407144a74a7f96a996467e6504e3"
CLIENT_SECRET = "339b63d9bf674a5eb6dde2f97d6496d3"
REDIRECT_URI = "https://open.spotify.com/"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="Ritesh"))

try:
    user_id = sp.current_user()["id"]
    print(f"User ID: {user_id}")
except spotipy.exceptions.SpotifyException as e:
    print(f"Spotify API error: {e}")
    exit()
except Exception as e:
    print(f"General error: {e}")
    exit()

# Scrape Billboard Hot 100
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)

# Fetching song title
song_html = response.text
soup = BeautifulSoup(song_html, "html.parser")
songs = soup.select(" li ul li h3")

songs_title = [song.getText().strip() for song in songs]
print("Top songs from Billboard Hot 100:")

for idx, title in enumerate(songs_title, start=1):
    print(f"{idx}. {title}")

# Search song on Spotify
print("\n Searching spotify for songs URIs")
song_uris = []
year = travel_date.split("-")[0]

for song in songs_title:
    try:
        query = f"track:{song} year:{year}"
        results = sp.search(q=query, type="track", limit=1)
        uri = results['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"Song '{song}' not found on spotify.")

#Display the song uris
print("\n list of Spotify URis")
pprint(song_uris)

# Creating an playlist in spotify and add songs
playlist_name= f"BillBoard Hot 100 - {travel_date}"
try:
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public= False)
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    print(f"Playlist '{playlist_name}' created successfully.")
except Exception as e:
    print(f"Error Creating playlis: {e}")