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


def country_feature_barplot(feature, countries=[]):
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    means = []
    labels = []
    for country in countries:
        data = get_country_csv(country)
        means.append(data[feature].mean())
        labels.append(country)

    sns.barplot(x=labels, y=means, palette='deep')
    plt.title('Music ' + feature + ' in Countries by Spotify')
    plt.xlabel('Country')
    plt.ylabel(feature)
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
    country_feature_barplot('speechiness', ['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    country_feature_barplot('loudness', ['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    country_feature_barplot('liveness', ['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    country_feature_barplot('acousticness', ['UnitedStates', 'Indonesia', 'Brazil', 'Mexica', 'Japan'])
    danceability_graph(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    #create_yearly_features_dotplot("danceability", "loudness")
    country_feature_barplot("loudness", ["Australia", "UnitedStates"])
    country_feature_barplot("loudness")