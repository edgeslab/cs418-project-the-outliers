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
    "CzechRepublicTop50": "37i9dQZEVXbIP3c3fqVrJY",
    "DenmarkTop50": "37i9dQZEVXbL3J0k32lWnN",
    "DominicanRepublicTop50": "37i9dQZEVXbKAbrMR8uuf7",
    "EcuadorTop50": "37i9dQZEVXbJlM6nvL1nD1",
    "ElSalvadorTop50": "37i9dQZEVXbLxoIml4MYkT",
    "EstoniaTop50": "37i9dQZEVXbLesry2Qw2xS",
    "FinlandTop50": "37i9dQZEVXbMxcczTSoGwZ",
    "FranceTop50": "37i9dQZEVXbIPWwFssbupI",
    "GermanyTop50": "37i9dQZEVXbJiZcmkrIHGU",
    "GreeceTop50": "37i9dQZEVXbJqdarpmTJDL",
    "GuatemalaTop50": "37i9dQZEVXbLy5tBFyQvd4",
    "HondurasTop50": "37i9dQZEVXbJp9wcIM9Eo5",
    "HongKongTop50": "37i9dQZEVXbLwpL8TjsxOG",
    "HungaryTop50": "37i9dQZEVXbNHwMxAkvmF8",
    "IcelandTop50": "37i9dQZEVXbKMzVsSGQ49S",
    "IndonesiaTop50": "37i9dQZEVXbObFQZ3JLcXt",
    "IrelandTop50": "37i9dQZEVXbKM896FDX8L1",
    "IsraelTop50": "37i9dQZEVXbJ6IpvItkve3",
    "ItalyTop50": "37i9dQZEVXbIQnj7RRhdSX",
    "JapanTop50": "37i9dQZEVXbKXQ4mDTEBXq",
    "LavtiaTop50": "37i9dQZEVXbJWuzDrTxbKS",
    "LithuaniaTop50": "37i9dQZEVXbMx56Rdq5lwc",
    "LuxembourgTop50": "37i9dQZEVXbKGcyg6TFGx6",
    "MalaysiaTop50": "37i9dQZEVXbJlfUljuZExa",
    "MexicaTop50": "37i9dQZEVXbO3qyFxbkOE1",
    "NetherlandsTop50": "37i9dQZEVXbKCF6dqVpDkS",
    "NewZealandTop50": "37i9dQZEVXbIPWwFssbupI",
    "NicaraguaTop50": "37i9dQZEVXbISk8kxnzfCq",
    "NorwayTop50": "37i9dQZEVXbJvfa0Yxg7E7",
    "PanamaTop50": "37i9dQZEVXbKypXHVwk1f0",
    "PeruTopTop50": "37i9dQZEVXbJfdy5b0KP7W",
    "PhilippinesTop50": "37i9dQZEVXbNBz9cRCSFkY",
    "PolandTop50": "37i9dQZEVXbN6itCcaL3Tt",
    "PortugalTop50": "37i9dQZEVXbKyJS56d1pgi",
    "RomaniaTop50": "37i9dQZEVXbNZbJ6TZelCq",
    "SingaporeTop50": "37i9dQZEVXbK4gjvS1FjPY",
    "SlovakiaTop50": "37i9dQZEVXbKIVTPX9a2Sb",
    "SouthAfricaTop50": "37i9dQZEVXbMH2jvi6jvjk",
    "SpainTop50": "37i9dQZEVXbNFJfN1Vw8d9",
    "SwedenTop50": "37i9dQZEVXbLoATJ81JYXz",
    "SwitzerlandTop50": "37i9dQZEVXbJiyhoAPEfMK",
    "TaiwanTop50": "37i9dQZEVXbMnZEatlMSiu",
    "ThailandTop50": "37i9dQZEVXbMnz8KIWsvf9",
    "TurkeyTop50": "37i9dQZEVXbIVYVBNw9D5K",
    "UnitedKingdomTop50": "37i9dQZEVXbLnolsZ8PSNw",
    "UruguayTop50": "37i9dQZEVXbMJJi3wgRbAy",
    "VietnamTop50": "37i9dQZEVXbLdGSmz6xilI",
    "UnitedStatesTop50": "37i9dQZEVXbLRQDuF5jeBp", 
}

for country in top_playlists_per_country.keys():
    country_playlist_features = main.get_playlist_audio_features(
        top_playlists_per_country[country], access_token)
    main.export_to_csv(
        "top50csv/"+country+".csv", country_playlist_features)
