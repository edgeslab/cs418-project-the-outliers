# Start of main
import io
import time
import json
import csv
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


def get_from_api(url, access_token):
    """
    Issue a get request to url using the access_token provided
    Args:
        url(string): the URL endpoint to GET
        access_token: the access token to use for authentication
    Returns:
        json response
    """
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    return response.json()

def get_playlist_audio_features(playlist_id, access_token):
    """
    Returns the list of playlist features for each track in the playlist_id provided
    Args: 
        playlist_id(string): the playlist_id to get from spotify
        access_token(string): the access token to use
    Returns:
        list of Audio Features objects per track in the playlist
        https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/
    """
    playlist = get_playlist(playlist_id, access_token)
    playlist_tracks = get_playlist_tracks(playlist)
    return get_audio_features(playlist_tracks, access_token)

def get_playlist(playlist_id, access_token):
    """
    Make an authenticated request to the Spotify API for the requested playlist ID.

    Args:
        playlist_id (string): the playlist_id to get

    Returns:
        A playlist object from spotify, see speck here
        https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-object-simplified
    """
    url = "https://api.spotify.com/v1/playlists/" + playlist_id
    return get_from_api(url, access_token)


def get_playlist_tracks(playlist_object):
    """
    Gets the tracks in the playlist object specified

    Args:
        playlist_object(dictionary): https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-object-simplified

    Returns:
        a list of the tracks in that object sorted by popularity
    """

    # all_tracks is a paging object:
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#paging-object
    all_tracks = playlist_object["tracks"]

    # TODO: alltracks is a paginated object, go over all of the pages in the playlist to get everything

    # the items in the object are playlist track objects:
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-track-object
    tracks = []
    for t in all_tracks["items"]:
        track = t["track"]
        tracks.append(track)
        print(track["name"])

    tracks.sort(key=lambda x: x["popularity"], reverse=True)
    return tracks


def get_audio_features(tracks, access_token):
    """
    Get the audio features of the provided tracks list

    Args:
        tracks(list, track objects): A list of track objects 
        https://developer.spotify.com/documentation/web-api/reference/object-model/#track-object-full
        access_token(string): the access token to use to make api requests.
    Returns:
        a list of the audio features each object has
        https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/
    """
    # TODO: if there are more than 100 tracks, spotify will either truncate or fail the request
    # implement pagination
    ids = ""
    for t in tracks:
        ids = ids + t['id'] + ','

    url = "https://api.spotify.com/v1/audio-features?ids=" + ids
    data = get_from_api(url, access_token)
    return data[next(iter(data))]


def export_to_csv(filename, list):
    
    #print (list)
    
    with open(filename, mode='w') as csv_file:
        colNames = list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=colNames)

        writer.writeheader()
        for record in list:
            writer.writerow(record)



print(api_key.client_key)
print(api_key.client_secret)
access_token = get_access_token()

# Rap Caviar Playlist
rap_caviar_audio_features = get_playlist_audio_features("37i9dQZF1DX0XUsuxWHRQd", access_token)
export_to_csv('rap_caviar_audio_features.csv',rap_caviar_audio_features)