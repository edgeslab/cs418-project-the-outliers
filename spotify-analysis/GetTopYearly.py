import main
import time
import json

access_token = main.get_access_token()

top_playlists_per_year = {
    "2018TopTracks": "37i9dQZF1DX1HUbZS4LEyL",
    "2017TopTracks": "37i9dQZF1DX7Axsg3uaDZb",  # USA
    "2016TopTracks": "2xKlsGov0EC2fhl6uXDgWZ",
    "2015TopTracks": "0q08gCS3oLglKH1Fan2s5V",
    "2014TopTracks": "37i9dQZF1DX4nHG0JvZ9Ht",  # USA
    "2013TopTracks": "7yBEqyAywWfxigN2Wj2UeI",  # USA
    "2012TopTracks": "3umOgg13I8RjiT3QCB6ogo",  # USA 
    "2011TopTracks": "42004WRNg430hY1cShpTsR",  # USA 
    "2010TopTracks": "0JnJKrKjU6BHVm8D2AyLvm", 
    "2000sTopTracks": "2f6tXtN0XesjONxicAzMIw",
    "1980sTopTracks": "37i9dQZF1DXb57FjYWz00c",
    "1970sTopTracks": "37i9dQZF1DWTJ7xPn4vNaz",
    "1960sTopTracks": "37i9dQZF1DXaKIA8E7WcJj",
    "1950sTopTracks": "37i9dQZF1DWSV3Tk4GO2fq",
    "1920sTopTracks": "7IFAfqFIn1smkwYYqQmJr2"
}

def createYearlyCSVs():
    for year in top_playlists_per_year.keys():
        yearly_playlist_features = main.get_playlist_audio_features(
            top_playlists_per_year[year], access_token)
        main.export_to_csv(
            "topTracksYearsCSV/"+year+".csv", yearly_playlist_features)

if __name__ == "__main__":
    createYearlyCSVs()