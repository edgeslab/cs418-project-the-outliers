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
    Opens the TopTracks.csv file for the year provided.

    Args:
        country(string): the year to open
    Returns:
        pandas dataset
    """
    return get_csv('topTracksYearsCSV/' + year + "TopTracks.csv")

def makeDanceabilityBarPlot(countrya, countryb):
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

def makeLoudnessBarplot(countrya, countryb):
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
    all_data = pd.DataFrame()
    for year in GetTopYearly.top_playlists_per_year:
        year_pd = get_yearly_csv(year)
        year_pd["year"] = year
        all_data = pd.concat([year_pd, all_data])
        
    # idk why but this stripplot function takes 5ever to run - I'm guessing its doing
    # a group_by underneath the hoods and that is what is causing the execution to
    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="year")
    plt.title("Yearly data " + featurea + ' VS ' + featureb )
    plt.legend(bbox_to_anchor=(-.05,1.05), loc="upper right")
    plt.show()

def create_country_features_dotplot(featurea, featureb, countries=[]):
    """
    Creates a dot plot outline of the features provided for all of the yearly data
    """
    if len(countries) == 0:
        countries = GetTop50Country.top_playlists_per_country.keys()

    all_data = pd.DataFrame()
    for country in countries:
        country_pd = get_country_csv(country)
        country_pd["country"] = country
        all_data = pd.concat([country_pd, all_data])
        
    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="country")
    plt.title("Country data " + featurea + ' VS ' + featureb )
    plt.legend(bbox_to_anchor=(-.05,1.05), loc="upper right")
    plt.show()

if __name__ == "__main__":
    create_yearly_features_dotplot("danceability", "loudness")
    makeDanceabilityBarPlot("Australia", "UnitedStates")
    makeLoudnessBarplot("Australia", "UnitedStates")
    make_country_barplot("loudness")
    create_country_features_dotplot("loudness", "danceability", ["UnitedStates", "Spain", "Sweden", "NewZealand", "Mexica"])
