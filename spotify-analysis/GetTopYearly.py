import main
import time
import json

access_token = main.get_access_token()

top_playlists_per_year = {
    "2018": "37i9dQZF1DX1HUbZS4LEyL",
    "2017": "37i9dQZF1DX7Axsg3uaDZb",  # USA
    "2016": "2xKlsGov0EC2fhl6uXDgWZ",
    "2015": "0q08gCS3oLglKH1Fan2s5V",
    "2014": "37i9dQZF1DX4nHG0JvZ9Ht",  # USA
    "2013": "7yBEqyAywWfxigN2Wj2UeI",  # USA
    "2012": "3umOgg13I8RjiT3QCB6ogo",  # USA 
    "2011": "42004WRNg430hY1cShpTsR",  # USA 
    "2010": "0JnJKrKjU6BHVm8D2AyLvm", 
    "2000s": "2f6tXtN0XesjONxicAzMIw",
    "1980s": "37i9dQZF1DXb57FjYWz00c",
    "1970s": "37i9dQZF1DWTJ7xPn4vNaz",
    "1960s": "37i9dQZF1DXaKIA8E7WcJj",
    "1950s": "37i9dQZF1DWSV3Tk4GO2fq",
    "1920s": "7IFAfqFIn1smkwYYqQmJr2"
}

def createYearlyCSVs():
    for year in top_playlists_per_year.keys():
        yearly_playlist_features = main.get_playlist_audio_features(
            top_playlists_per_year[year], access_token)
        main.export_to_csv(
            "topTracksYearsCSV/"+year+"TopTracks.csv", yearly_playlist_features)

if __name__ == "__main__":
    createYearlyCSVs()