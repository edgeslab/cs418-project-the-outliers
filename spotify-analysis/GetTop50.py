import main
import time
import json

access_token = main.get_access_token()

top_playlists_per_country = {
    "ArgentinaTop50": "37i9dQZEVXbMMy2roB9myp",
    "AustraliaTop50": "37i9dQZEVXbJPcfkRz0wJ0",
    "AustriaTop50": "37i9dQZEVXbKNHh6NIXu36",
    "BelgiumTop50": "37i9dQZEVXbJNSeeHswcKB",
    "BoliviaTop50": "37i9dQZEVXbJqfMFK4d691",
    "BrazilTop50": "37i9dQZEVXbMXbN3EUUhlg",
    "BulgariaTop50": "37i9dQZEVXbNfM2w2mq1B8",
    "CanadaTop50": "37i9dQZEVXbKj23U1GF4IR",
    "ChilleTop50": "37i9dQZEVXbL0GavIqMTeb",
    "ColumbiaTop50": "37i9dQZEVXbOa2lmxNORXQ",
    "CostaRicaTop50": "37i9dQZEVXbMZAjGMynsQX",
    "UnitedStatesTop50": "37i9dQZEVXbLRQDuF5jeBp"
}

for country in top_playlists_per_country.keys():
    country_playlist_features = main.get_playlist_audio_features(
        top_playlists_per_country[country], access_token)
    main.export_to_csv(
        "top50csv/"+country+".csv", country_playlist_features)
