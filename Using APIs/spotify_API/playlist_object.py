import requests

def get_playlist_object(playlist_url, access_token):
    """
    playlist_url : url of spotify playlist
    access_token : access token gotten from client credentials authorization
    
    return object containing playlist tracks
    """
    playlist_id = playlist_url.split("/")[-1]
    playlist_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    get_header = {
    "Authorization" : "Bearer " + access_token
    }
    
    # API request
    response = requests.get(playlist_endpoint, headers=get_header)
    playlist_object = response.json()
    
    return playlist_object