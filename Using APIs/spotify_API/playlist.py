import pandas as pd

def get_playlist(df):
    """
    df: empty pandas dataframe
    
    return dataframe containing playlist
    """
    for i in range(len(playlist_object["tracks"]["items"])):
        song = playlist_object["tracks"]["items"][i]["track"]["album"]["name"]

        song_id = playlist_object["tracks"]["items"][i]["track"]["id"]

        duration_ms = playlist_object["tracks"]["items"][i]["track"]["duration_ms"]

        popularity = playlist_object["tracks"]["items"][i]["track"]["popularity"]

        release_date = playlist_object["tracks"]["items"][i]["track"]["album"]["release_date"]

        artists = [(name["name"],name["id"]) for name in playlist_object["tracks"]["items"][i]["track"]["album"]["artists"]]
        artist = artists[0][0]
        artist_id = artists[0][1]
        if len(artists) > 1:
            featured_artist = artists[1][0]
            featured_artist_id = artists[1][1]
        if len(artists) > 2:
            featured_artist = (artists[1][0],artists[2][0])
            featured_artist_id = (artists[1][1], artists[2][1])

        df = df.append({
        df.columns[0]:song,
        df.columns[1]:song_id,
        df.columns[2]:duration_ms,
        df.columns[3]:popularity,
        df.columns[4]:release_date,
        df.columns[5]:artist,
        df.columns[6]:artist_id, 
        df.columns[7]:featured_artist, 
        df.columns[8]:featured_artist_id
        },ignore_index=True)

    return df