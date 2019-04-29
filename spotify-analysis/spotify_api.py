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

def get_song_audio_features(song_id, access_token=""):
    if access_token == "": 
        access_token = get_access_token()

    url = "https://api.spotify.com/v1/audio-features/" + song_id
    data =  get_from_api(url, access_token)
    return data


def get_playlist_audio_features(playlist_id, access_token=""):
    """
    Returns the list of playlist features for each track in the playlist_id provided
    Args: 
        playlist_id(string): the playlist_id to get from spotify
        access_token(string): the access token to use, if empty, will regenrate a new access_token
    Returns:
        list of Audio Features objects per track in the playlist
        https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/
    """
    if access_token == "": 
        access_token = get_access_token()
    
    playlist = get_playlist(playlist_id, access_token)
    playlist_tracks = get_playlist_tracks(playlist, access_token)
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


def get_playlist_tracks(playlist_object, access_token):
    """
    Gets the tracks in the playlist object specified, including multiple pages, since all_tracks is a paging object

    Args:
        playlist_object(dictionary): https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-object-simplified

    Returns:
        a list of the tracks in that object sorted by popularity
    """

    # the items in the object are playlist track objects:
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#playlist-track-object   
    tracks_response = playlist_object["tracks"]
    tracks = []

    items = tracks_response["items"]
    while len(items) > 0:
        for t in items:
            tracks.append(t["track"])

        # get next page 
        if tracks_response["next"] is not None:
            tracks_response = get_from_api(tracks_response["next"], access_token)
            items = tracks_response["items"]
        else:
            items = []

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
    partial_tracks = tracks
    final_result = []

    while len(partial_tracks) > 0:
        n = min(len(partial_tracks), 100)
    
        partial_ids = ""

        for t in partial_tracks[:n]:
            partial_ids = partial_ids + t['id'] + ','

        url = "https://api.spotify.com/v1/audio-features?ids=" + partial_ids   # gets id's 0 - 100
        partial_response = get_from_api(url, access_token)

        # gets all dictionaries and puts into one list - gets rid of outside wrapper
        partial_response_list = partial_response[next(iter(partial_response))]

        for track in partial_response_list:
            final_result.append(track)
        # If there are more than 100 tracks, get the next sets of audio features in a loop
        partial_tracks = partial_tracks[(n+1):]

    return final_result


def get_track_genre(track, access_token):
    """
    Get the genre of the provided track

    Args:
        track(track objects): A track object
        https://developer.spotify.com/documentation/web-api/reference/object-model/#track-object-full
        access_token(string): the access token to use to make api requests.
    Returns:
        the genre(s) as a list of strings
    """
    # get the track's artists and retrieve their genres
    genres = []
    artists = track['artists']

    for a in artists:
        url = 'https://api.spotify.com/v1/artists/' + a['id']
        response = get_from_api(url, access_token)
        genres.extend(response['genres'])
   
    return genres


def export_to_csv(filename, list):
    """
    Get the audio features of the provided tracks list

    Args:
        filename(string): The name of the csv file to be created
        list(list, dictionary objects): The list of data extracted from json to be put into a csv file.   
    Output:
        a csv file with the indicated name   
    """
    with open(filename, mode='w') as csv_file:
        colNames = list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=colNames)

        writer.writeheader()
        for record in list:
            writer.writerow(record)

def export_pd_to_csv(filename, dataframe):
    dataframe.to_csv(filename)

if __name__ == "__main__":
    access_token = get_access_token()
    # Fatima's playlist which has 178 songs (test pagination)
    fatima_top_178 = get_playlist_audio_features("2xF8OfOFpFbojipxPndAL5", access_token)
    export_to_csv('testPlaylistsCSV/fatimaTop178.csv', fatima_top_178)
