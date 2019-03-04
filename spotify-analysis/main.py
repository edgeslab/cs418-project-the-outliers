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
        A playlist object from spotify, see speck here
        https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-object-simplified
    """
    url = "https://api.spotify.com/v1/playlists/" + playlist_id
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)

    json = response.json()
    return json

def get_playlist_tracks(playlist_object):
    """
    Gets the tracks in the playlist object specified

    Args:
        playlist_object(dictionary): https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-object-simplified
    
    Returns:
        a list of the tracks in that object
    """

    # all_tracks is a paging object: 
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#paging-object
    all_tracks = playlist_object["tracks"]

    # the items in the object are playlist track objects: 
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-track-object
    tracks = []
    for t in all_tracks["items"]:
        track = t["track"]
        tracks.append(track)
        print(track["name"])
    return tracks


print(api_key.client_key)
print(api_key.client_secret)
access_token = get_access_token()

# Rap Caviar Playlist
rap_caviar_playlist = get_playlist("37i9dQZF1DX0XUsuxWHRQd", access_token)
rap_caviar_tracks = get_playlist_tracks(rap_caviar_playlist)
