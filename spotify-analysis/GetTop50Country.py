import spotify_api
import time
import json

access_token = spotify_api.get_access_token()

top_playlists_per_country = {
    "Argentina": "37i9dQZEVXbMMy2roB9myp",
    "Australia": "37i9dQZEVXbJPcfkRz0wJ0",
    "Austria": "37i9dQZEVXbKNHh6NIXu36",
    "Belgium": "37i9dQZEVXbJNSeeHswcKB",
    "Bolivia": "37i9dQZEVXbJqfMFK4d691",
    "Brazil": "37i9dQZEVXbMXbN3EUUhlg",
    "Bulgaria": "37i9dQZEVXbNfM2w2mq1B8",
    "Canada": "37i9dQZEVXbKj23U1GF4IR",
    "Chille": "37i9dQZEVXbL0GavIqMTeb",
    "Columbia": "37i9dQZEVXbOa2lmxNORXQ",
    "CostaRica": "37i9dQZEVXbMZAjGMynsQX",
    "CzechRepublic": "37i9dQZEVXbIP3c3fqVrJY",
    "Denmark": "37i9dQZEVXbL3J0k32lWnN",
    "DominicanRepublic": "37i9dQZEVXbKAbrMR8uuf7",
    "Ecuador": "37i9dQZEVXbJlM6nvL1nD1",
    "ElSalvador": "37i9dQZEVXbLxoIml4MYkT",
    "Estonia": "37i9dQZEVXbLesry2Qw2xS",
    "Finland": "37i9dQZEVXbMxcczTSoGwZ",
    "France": "37i9dQZEVXbIPWwFssbupI",
    "Germany": "37i9dQZEVXbJiZcmkrIHGU",
    "Greece": "37i9dQZEVXbJqdarpmTJDL",
    "Guatemala": "37i9dQZEVXbLy5tBFyQvd4",
    "Honduras": "37i9dQZEVXbJp9wcIM9Eo5",
    "HongKong": "37i9dQZEVXbLwpL8TjsxOG",
    "Hungary": "37i9dQZEVXbNHwMxAkvmF8",
    "Iceland": "37i9dQZEVXbKMzVsSGQ49S",
    "Indonesia": "37i9dQZEVXbObFQZ3JLcXt",
    "Ireland": "37i9dQZEVXbKM896FDX8L1",
    "Italy": "37i9dQZEVXbIQnj7RRhdSX",
    "Japan": "37i9dQZEVXbKXQ4mDTEBXq",
    "Lavtia": "37i9dQZEVXbJWuzDrTxbKS",
    "Lithuania": "37i9dQZEVXbMx56Rdq5lwc",
    "Luxembourg": "37i9dQZEVXbKGcyg6TFGx6",
    "Malaysia": "37i9dQZEVXbJlfUljuZExa",
    "Mexica": "37i9dQZEVXbO3qyFxbkOE1",
    "Netherlands": "37i9dQZEVXbKCF6dqVpDkS",
    "NewZealand": "37i9dQZEVXbIPWwFssbupI",
    "Nicaragua": "37i9dQZEVXbISk8kxnzfCq",
    "Norway": "37i9dQZEVXbJvfa0Yxg7E7",
    "Panama": "37i9dQZEVXbKypXHVwk1f0",
    "PeruTop": "37i9dQZEVXbJfdy5b0KP7W",
    "Philippines": "37i9dQZEVXbNBz9cRCSFkY",
    "Poland": "37i9dQZEVXbN6itCcaL3Tt",
    "Portugal": "37i9dQZEVXbKyJS56d1pgi",
    "Romania": "37i9dQZEVXbNZbJ6TZelCq",
    "Singapore": "37i9dQZEVXbK4gjvS1FjPY",
    "Slovakia": "37i9dQZEVXbKIVTPX9a2Sb",
    "SouthAfrica": "37i9dQZEVXbMH2jvi6jvjk",
    "Spain": "37i9dQZEVXbNFJfN1Vw8d9",
    "Sweden": "37i9dQZEVXbLoATJ81JYXz",
    "Switzerland": "37i9dQZEVXbJiyhoAPEfMK",
    "Taiwan": "37i9dQZEVXbMnZEatlMSiu",
    "Thailand": "37i9dQZEVXbMnz8KIWsvf9",
    "Turkey": "37i9dQZEVXbIVYVBNw9D5K",
    "UnitedKingdom": "37i9dQZEVXbLnolsZ8PSNw",
    "Uruguay": "37i9dQZEVXbMJJi3wgRbAy",
    "Vietnam": "37i9dQZEVXbLdGSmz6xilI",
    "UnitedStates": "37i9dQZEVXbLRQDuF5jeBp", 
}

def createCountryCSVs():
    for country in top_playlists_per_country.keys():
        country_playlist_features = spotify_api.get_playlist_audio_features(
            top_playlists_per_country[country], access_token)
        spotify_api.export_to_csv(
            "top50CountryCSV/"+country+"Top50.csv", country_playlist_features)

if __name__ == "__main__":
    createCountryCSVs()
