import spotify_api
import time
import json
import pandas as pd

access_token = spotify_api.get_access_token()

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
    all_years = pd.DataFrame()	   
    for year in top_playlists_per_year.keys():	    
        yearly_playlist_features = spotify_api.get_playlist_audio_features(	      
            top_playlists_per_year[year], access_token)	           
        year_pd = pd.DataFrame(yearly_playlist_features)	       
        year_pd["year"] = year	      
        all_years = all_years.append(year_pd)	
    spotify_api.export_pd_to_csv(
        "topTracksYearsCSV/AllYearsTopTracks.csv", all_years)

if __name__ == "__main__":
    createYearlyCSVs()