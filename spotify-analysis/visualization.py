import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import GetTopYearly
import GetTop50Country

matplotlib.rcParams['figure.figsize'] = [10, 5]

def get_csv(filename):
    return pd.read_csv(filename)

def get_country_csv(country):
    """
    Opens the Top50.csv file for the country provided.

    Args:
        country(string): the country to open
    Returns:
        pandas dataset
    """
    return get_csv('top50CountryCSV/' + country + "Top50.csv")

def get_yearly_csv(year):
    """
    Opens the Top50.csv file for the year provided.

    Args:
        country(string): the country to open
    Returns:
        pandas dataset
    """
    return get_csv('topTracksYearsCSV/' + year + "TopTracks.csv")

def make_danceability_barplot(countrya, countryb):
    """
    Creates a seaborn distribution plot for the dancability of the
    two countries provided.

    Args:
        countrya, countryb (string): the two countries to compare
    """
    countryAcsv = get_country_csv(countrya)
    countryBcsv = get_country_csv(countryb)
    sns.distplot(countryAcsv['danceability'], label=countrya + ' Danceability',)
    sns.distplot(countryBcsv['danceability'], label=countryb + ' Danceability')
    plt.title(countrya + ' VS ' + countryb + ' danceability')
    plt.xlabel('Danceability')
    plt.legend()
    plt.show()

def make_country_barplot(feature, countries=[]):
    """
    Creates a seaborn distribution plot for the loudness of the
    two countries provided.

    Args:
        feature(string): the feature to plot
        countries(list, string): the countries to compare
    """
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    for country in countries:
        countrycsv = get_country_csv(country)
        sns.distplot(countrycsv[feature], label=country)

    plt.title(feature + ' by country')
    plt.xlabel(feature)
    if(len(countries) < 10):
        plt.legend()
    plt.show()

def make_loudness_barplot(countrya, countryb):
    """
    Creates a seaborn distribution plot for the loudness of the
    two countries provided.

    Args:
        countrya, countryb (string): the two countries to compare
    """
    countryAcsv = get_country_csv(countrya)
    countryBcsv = get_country_csv(countryb)
    sns.distplot(countryAcsv['loudness'], label=countrya + ' Loudness')
    sns.distplot(countryBcsv['loudness'], label=countryb + ' Loudness')
    plt.title(countrya + ' VS ' + countryb + ' loudness')
    plt.xlabel('Loudness')
    plt.legend()
    plt.show()

def create_yearly_features_dotplot(featurea, featureb):
    """
    Creates a dot plot outline of the features provided for all of the yearly data
    """
    all_data = get_csv('topTracksYearsCSV/AllYearsTopTracks.csv')

    # idk why but this stripplot function takes 5ever to run - I'm guessing its doing
    # a group_by underneath the hoods and that is what is causing the execution to
    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="year")
    plt.title("Yearly data " + featurea + ' VS ' + featureb)
    plt.legend(bbox_to_anchor=(-.05, 1.05), loc="upper right")
    plt.show()

def create_country_features_dotplot(featurea, featureb, countries=[]):
    """
    Creates a dot plot outline of the features provided for all of the yearly data
    """
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    all_data = get_csv('topTracksYearsCSV/AllYearsTopTracks.csv')

    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="country")
    plt.title("Country data " + featurea + ' VS ' + featureb)
    plt.legend(bbox_to_anchor=(-.05, 1.05), loc="upper right")
    plt.show()

def liveness_graph(countries=[]):
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    liveness_means = []
    country_list = []

    for country in countries:
        data = get_country_csv(country)
        liveness_means.append(data['liveness'].mean())
        country_list.append(country)

    sns.barplot(x=country_list, y=liveness_means, palette='deep')
    plt.title('Music Liveness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Liveness')
    plt.show()


def acousticness_graph(countries=[]):
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    acousticness_means = []
    country_list = []
    for country in countries:
        data = get_country_csv(country)
        acousticness_means.append(data['acousticness'].mean())
        country_list.append(country)

    sns.barplot(x=country_list, y=acousticness_means, palette='deep')
    plt.title('Music Acousticness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Acousticness')
    plt.show()


def danceability_graph(years=[]):
    if len(years) == 0:
        years = GetTopYearly.top_playlists_per_year.keys()

    danceability_means = []

    for year in years:
        data = get_yearly_csv(year)
        danceability_means.append(data['danceability'].mean())

    sns.pointplot(x=years, y=danceability_means, label="Danceabillity", linestyle="-")
    plt.title('Danceability of Top Songs From 2010-2018')
    plt.xlabel('Years')
    plt.ylabel('Danceability')
    plt.show()


def duration_graph(years=[]):
    if len(years) == 0:
        years = GetTopYearly.top_playlists_per_year.keys()

    duration_means = []
    for year in years:
        data = get_yearly_csv(year)
        duration_means.append(data['duration_ms'].mean())

    sns.pointplot(x=years, y=duration_means, label="Duration", linestyle="-")
    plt.title('Duration of Top Songs From 2010-2018')
    plt.xlabel('Years')
    plt.ylabel('Duration')
    plt.show()


def loudness_graph(countries=[]):
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    loudness_means = []
    country_list = []
    for country in countries:
        data = get_country_csv(country)
        loudness_means.append(data['loudness'].mean())
        country_list.append(country)

    sns.barplot(x=country_list, y=loudness_means, palette='deep')
    plt.title('Music Loudness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Loudness')
    plt.show()


def speechiness_graph(countries=[]):
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    speechiness_means = []
    country_list = []
    for country in countries:
        data = get_country_csv(country)
        speechiness_means.append(data['speechiness'].mean())
        country_list.append(country)

    sns.barplot(x=country_list, y=speechiness_means, palette='deep')
    plt.title('Music Speechiness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Speechiness')
    plt.show()


def dance_vs_energy_graph(years=[]):
    if len(years) == 0:
        years = GetTopYearly.top_playlists_per_year.keys()

    data = pd.DataFrame()
    for year in years:
        year_data = get_yearly_csv(year)
        features = [
            {'feature': 'danceability', 'mean': year_data['danceability'].mean(), 'year':year },  
            {'feature': 'energy', 'mean': year_data['energy'].mean(), 'year':year }
        ]
        data = data.append(pd.io.json.json_normalize(features))

    sns.pointplot(x="year", y="mean", data=data, hue="feature", linestyle="-", color='purple')
    plt.title('Danceability VS Energy of Top Songs From 2010-2018')
    plt.xlabel('year')
    plt.ylabel('Dance VS Energy')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    duration_graph(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    dance_vs_energy_graph(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    speechiness_graph(['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    loudness_graph(['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    liveness_graph(['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    acousticness_graph(['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    danceability_graph(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    create_yearly_features_dotplot("danceability", "loudness")
    make_danceability_barplot("Australia", "UnitedStates")
    make_loudness_barplot("Australia", "UnitedStates")
    make_country_barplot("loudness")
    create_country_features_dotplot("loudness", "danceability", ["UnitedStates", "Spain", "Sweden", "NewZealand", "Mexica"])
