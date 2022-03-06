import auth
import os
import pandas as pd
import playlist  
import playlist_object

# import client credentials
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

# hot hits naija url : https://open.spotify.com/playlist/37i9dQZF1DWZCOSaet9tpB
url = "https://open.spotify.com/playlist/37i9dQZF1DWZCOSaet9tpB"
token = auth.get_access_token(client_id, client_secret)
playlist_object = playlist_object.get_playlist_object(url, token)

df = pd.DataFrame(columns = ['song','song_id','duration_ms','popularity','release_date','artist', 'artist_id', 'featured_artist', 'featured_artist_id'])
playlist = playlist.get_playlist(df)

playlist = (
    playlist
    .assign(duration_mins = lambda x :(x['duration_ms'])/(1000*60))
    .assign(release_date = lambda x : pd.to_datetime(x['release_date']))
    .drop(columns='duration_ms')
)
playlist.head()