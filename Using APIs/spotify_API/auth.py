import base64
import json
import requests

def get_access_token(client_id, client_secret):
    """
    client_id : spotify client ID
    client_secrete : spotify client SECRET
    
    return access token
    """
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = {}
    auth_data = {}

    # Base64 encode client_id and client_secret

    message = f"{client_id}:{client_secret}"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    # Authorization: Basic <base64 encoded client_id:client_secret>

    auth_header["Authorization"] = "Basic " + base64_message
    auth_data["grant_type"] = "client_credentials"

    response = requests.post(auth_url, headers=auth_header, data=auth_data)
    response_object = response.json()
    json.dumps(response_object)
    access_token = response_object["access_token"]
    
    return access_token