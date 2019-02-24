# Start of main
import io
import time
import json
import requests
import api_key
import base64


def get_access_token():
    """
    Makes a request to the Spotify API to obtain an authorization token

    Returns:
        An acces token(string) that can be used to make requests to the Spotify application
    """
    url = "https://accounts.spotify.com/api/token"

    # The header of this POST request must contain the Authorization param.
    # Base 64 encoded string that contains the client ID and client secret key.
    # format: Authorization: Basic <base64 encoded client_id:client_secret>
    auth = api_key.client_key + ":" + api_key.client_secret
    header = {
        "Authorization": b'Basic ' + base64.b64encode(auth.encode())
    }

    # The body of this POST request must contain grant_type
    # in our case, grant_type = client_credentials since we will only access public data
    body = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url=url, headers=header, data=body)
    json = response.json()
    return json['access_token']


def get_playlist(playlist_id, access_token):
    """
    Make an authenticated request to the Spotify API for the requested playlist ID.

    Args:
        query (string): the playlist_id to get

    Returns:
        the contents of the playlist?
    """
    url = "https://api.spotify.com/v1/playlists/" + playlist_id
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)

    json = response.json()
    print(json)


print(api_key.client_key)
print(api_key.client_secret)
access_token = get_access_token()

# Rap Caviar Playlist
get_playlist("37i9dQZF1DX0XUsuxWHRQd", access_token)
