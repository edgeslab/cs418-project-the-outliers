import main
import time
import json

access_token = main.get_access_token()

top_playlists_per_year = {
    "2018TopTracks": "37i9dQZF1DX1HUbZS4LEyL",
    "2017TopTracks": "37i9dQZF1DX5nwnRMcdReF",
    "2015TopTracks": "0q08gCS3oLglKH1Fan2s5V",
    "50sTopTracks": "2pPGmv15Xs7sgvCywghrXZ"
}

for year in top_playlists_per_year.keys():
    country_playlist_features = main.get_playlist_audio_features(
        top_playlists_per_year[year], access_token)
    main.export_to_csv(
        "topTracksYearscsv/"+year+".csv", country_playlist_features)
