import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = 'http://127.0.0.1:5000/'
SCOPE = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

user = sp.current_user()

current_track = sp.current_user_playing_track()
print(current_track)
#print(f"{user['display_name']} is currently playing {current_track['item']['name']} by {current_track['item']['artists'][0]['name']}")
