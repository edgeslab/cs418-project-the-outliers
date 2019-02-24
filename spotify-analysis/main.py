# Start of main
import io, time, json
import requests
import api_key
import spotipy
import base64

def get_access_token():
    # First step is to request authorization
    # The body of this POST request must contain grant_type encoded in application/x-www-form-urlencoded. 
    # in our case, grant_type = client_credentials since we will only access public data
    # The header of this POST request must contain the following parameter:
    # Authorization. Base 64 encoded string that contains the client ID and client secret key.
    # The field must have the format: Authorization: Basic <base64 encoded client_id:client_secret>
    url = "https://accounts.spotify.com/api/token"
    auth = api_key.client_key+":"+api_key.client_secret

    header = {
        "Authorization": b'Basic ' + base64.b64encode(auth.encode())
    }

    body = {
        "grant_type" : "client_credentials"
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
    headers = {'Authorization':'Bearer ' + access_token}
    response = requests.get(url, headers = headers)

    json = response.json()
    print(json)

print(api_key.client_key)
print(api_key.client_secret)
access_token = get_access_token()
get_playlist("37i9dQZF1DX0XUsuxWHRQd", access_token)