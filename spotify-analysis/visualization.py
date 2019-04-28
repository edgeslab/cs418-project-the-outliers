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

def liveness_graph():
    # Retreiving US data from CSV files

    data_United_states = get_country_csv('UnitedStates')
    US_liveness = data_United_states['liveness']
    mean_us_liveness = US_liveness.mean()

    # Retreiving Indonesia data from CSV files

    data_Indonesia = pd.read_csv('Indonesia')
    indo_liveness = data_Indonesia['liveness']
    mean_Indo_liveness = indo_liveness.mean()

    # Retreiving Brazil data from CSV files

    data_Brazil = pd.read_csv('Brazil')
    brazil_liveness = data_Brazil['liveness']
    mean_Brazil_liveness = brazil_liveness.mean()

    # Retreiving Mexico data from CSV files

    data_Mexico = pd.read_csv('Mexica')
    Mexico_liveness = data_Mexico['liveness']
    mean_Mexico_liveness = Mexico_liveness.mean()

    # Retreiving Japan data from CSV files

    data_Japan = pd.read_csv('Japan')
    japan_liveness = data_Japan['liveness']
    mean_japan_liveness = japan_liveness.mean()

    # Creating the list of mean values

    mesn_liveness_list = [mean_us_liveness, mean_Indo_liveness, mean_Brazil_liveness, mean_Mexico_liveness,
                          mean_japan_liveness]

    # Declaring Labels for X axis

    Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

    # Plotting the graph

    bar_plot = sns.barplot(x=Country_labels, y=mesn_liveness_list, palette='deep')

    # Labelling the Graph

    plt.title('Music Liveness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Liveness')

    # Showing the Graph
    plt.show()

def acousticness_graph():
    # Getting the US data data from CSV files

    data_United_states = get_country_csv('UnitedStates')
    US_acousticness = data_United_states['acousticness']
    mean_us_acousticness = US_acousticness.mean()

    # Getting the Indonesia data from CSV files

    data_Indonesia = get_country_csv('Indonesia')
    indo_acousticness = data_Indonesia['acousticness']
    mean_Indo_acousticness = indo_acousticness.mean()

    # Getting the Brazil data from CSV files

    data_Brazil = get_country_csv('Brazil')
    brazil_acousticness = data_Brazil['acousticness']
    mean_Brazil_acousticness = brazil_acousticness.mean()

    # Getting the Mexico data from CSV files

    data_Mexico = get_country_csv('Mexica')
    Mexico_acousticness = data_Mexico['acousticness']
    mean_Mexico_acousticness = Mexico_acousticness.mean()

    # Getting the Japan data data from CSV files

    data_Japan = get_country_csv('Japan')
    japan_acousticness = data_Japan['acousticness']
    mean_japan_acousticness = japan_acousticness.mean()

    # Ca;culating mean and puttong it into list

    mean_acousticness_list = [mean_us_acousticness, mean_Indo_acousticness, mean_Brazil_acousticness,mean_Mexico_acousticness, mean_japan_acousticness]

    # Creating the labels for X axis

    Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

    # Plotting the Graph

    bar_plot = sns.barplot(x=Country_labels, y=mean_acousticness_list, palette='deep')

    # Labelling the Graph

    plt.title('Music Acousticness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Acousticness')

    # Showing the Graph

    plt.show()

def graph_danca_vs_energy():
    # Retreiving the data from CSV files

    data2010 = get_yearly_csv('2010')
    energy2010 = data2010['energy']
    data2011 = get_yearly_csv('2011')
    energy2011 = data2011['energy']
    data2012 = get_yearly_csv('2012')
    energy2012 = data2012['energy']
    data2013 = get_yearly_csv('2013')
    energy2013 = data2013['energy']
    data2014 = get_yearly_csv('2014')
    energy2014 = data2014['energy']
    data2015 = get_yearly_csv('2015')
    energy2015 = data2015['energy']
    data2016 = get_yearly_csv('2016')
    energy2016 = data2016['energy']
    data2017 = get_yearly_csv('2017')
    energy2017 = data2017['energy']
    data2018 = get_yearly_csv('2018')
    energy2018 = data2018['energy']

    danca2010 = data2010['danceability']
    data2011 = get_yearly_csv('2011')
    danca2011 = data2011['danceability']
    data2012 = get_yearly_csv('2012')
    danca2012 = data2012['danceability']
    data2013 = get_yearly_csv('2013')
    danca2013 = data2013['danceability']
    data2014 = get_yearly_csv('2014')
    danca2014 = data2014['danceability']
    data2015 = get_yearly_csv('2015')
    danca2015 = data2015['danceability']
    data2016 = get_yearly_csv('2016')
    danca2016 = data2016['danceability']
    data2017 = get_yearly_csv('2017')
    danca2017 = data2017['danceability']
    data2018 = get_yearly_csv('2018')
    danca2018 = data2018['danceability']

    # making the list of mean values of danceability and energy from the data

    lisy = [danca2010.mean(), danca2011.mean(), danca2012.mean(), danca2013.mean(), danca2014.mean(), danca2015.mean(),
            danca2016.mean(), danca2017.mean(), danca2018.mean()]
    list_Energy = [energy2010.mean(), energy2011.mean(), energy2012.mean(), energy2013.mean(), energy2014.mean(),
                   energy2015.mean(), energy2016.mean(), energy2017.mean(), energy2018.mean()]

    # Labelling X Axis

    year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

    # plotting thr graphs

    plot1 = sns.pointplot(x=year_labels, y=lisy, label='Danceability', color='purple')
    plot2 = sns.pointplot(x=year_labels, y=list_Energy, label='Energy', color='green')

    # Labelling the graphs

    plt.title('Danceability VS Energy of Top Songs From 2010-2018')
    plt.xlabel('Year')
    plt.ylabel('Danceability / Energy')
    plot1.legend(labels=['Danceability', 'Energy'], loc='upper left', ncol=2)

    # Showing the graph
    plt.show()

def graph_danceabillity():
    # Getting the data from the CSV files

    data2010 = get_yearly_csv('2010')
    danca2010 = data2010['danceability']
    data2011 = get_yearly_csv('2011')
    danca2011 = data2011['danceability']
    data2012 = get_yearly_csv('2012')
    danca2012 = data2012['danceability']
    data2013 = get_yearly_csv('2013')
    danca2013 = data2013['danceability']
    data2014 = get_yearly_csv('2014')
    danca2014 = data2014['danceability']
    data2015 = get_yearly_csv('2015')
    danca2015 = data2015['danceability']
    data2016 = get_yearly_csv('2016')
    danca2016 = data2016['danceability']
    data2017 = get_yearly_csv('2017')
    danca2017 = data2017['danceability']
    data2018 = get_yearly_csv('2018')
    danca2018 = data2018['danceability']

    # making a list of mean values of danceability of different countries

    lisy = [danca2010.mean(), danca2011.mean(), danca2012.mean(), danca2013.mean(), danca2014.mean(), danca2015.mean(),danca2016.mean(), danca2017.mean(), danca2018.mean()]

    # making list of year labels

    year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

    # plotting the graph

    plot = sns.pointplot(x=year_labels, y=lisy, label="Loudness", linestyle="-")

    # labelling the graph

    plt.title('Danceability of Top Songs From 2010-2018')
    plt.xlabel('Year')
    plt.ylabel('Danceability')
    plot.legend(['Danceability'])

    # showing the graph

    plt.show()



def graph_duration():
    # Getting data from CSV files

    data2010 = get_yearly_csv('2010')
    duration_2010 = data2010['duration_ms']
    data2011 = get_yearly_csv('2011')
    duration_2011 = data2011['duration_ms']
    data2012 = get_yearly_csv('2012')
    duration_2012 = data2012['duration_ms']
    data2013 = get_yearly_csv('2013')
    duration_2013 = data2013['duration_ms']
    data2014 = get_yearly_csv('2014')
    duration_2014 = data2014['duration_ms']
    data2015 = get_yearly_csv('2015')
    duration_2015 = data2015['duration_ms']
    data2016 = get_yearly_csv('2016')
    duration_2016 = data2016['duration_ms']
    data2017 = get_yearly_csv('2017')
    duration_2017 = data2017['duration_ms']
    data2018 = get_yearly_csv('2018')
    duration_2018 = data2018['duration_ms']

    # Making list of mean values of duration for consecutive years

    lisy = [duration_2010.mean(), duration_2011.mean(), duration_2012.mean(), duration_2013.mean(),
            duration_2014.mean(), duration_2015.mean(), duration_2016.mean(), duration_2017.mean(),
            duration_2018.mean()]

    # Label list for x Axis

    year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

    # Putting up title and labels

    plt.title('Duration of Top Songs From 2010-2018')
    plt.xlabel('Year')
    plt.ylabel('Duration in milisconds')

    # Plotting the graph

    sns.pointplot(x=year_labels, y=lisy, color='purple')

    # Showing the Graph

    plt.show()

def graph_loudness():
    # CSV file data accquisition of US

    data_United_states = get_country_csv('UnitedStates')
    US_loudness = data_United_states['loudness']
    mean_us_loudness = US_loudness.mean()

    # CSV file data accquisition of Indonesia

    data_Indonesia = get_country_csv('Indonesia')
    indo_loudness = data_Indonesia['loudness']
    mean_Indo_loudness = indo_loudness.mean()

    # CSV file data accquisition of Brazil

    data_Brazil = get_country_csv('Brazil')
    brazil_loudness = data_Brazil['loudness']
    mean_Brazil_loudness = brazil_loudness.mean()

    # CSV file data accquisition of Mexico

    data_Mexico = get_country_csv('Mexica')
    Mexico_loudness = data_Mexico['loudness']
    mean_Mexico_loudness = Mexico_loudness.mean()

    # CSV file data accquisition of Jaopan

    data_Japan = get_country_csv('Japan')
    japan_loudness = data_Japan['loudness']
    mean_japan_loudness = japan_loudness.mean()

    # Creating labels and calculating mean valeus

    mesn_loudness_list = [mean_us_loudness, mean_Indo_loudness, mean_Brazil_loudness, mean_Mexico_loudness,
                          mean_japan_loudness]
    Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

    # Plotting the barplot

    bar_plot = sns.barplot(x=Country_labels, y=mesn_loudness_list, palette='deep')

    # Puttom=ng up title and labels for graph

    plt.title('Music Loudness in Most Populated Countries in Spotify')
    plt.xlabel('Country')
    plt.ylabel('Loudness')

    # Showing the graph

    plt.show()

def graph_speechiness():
    # Getting US data from CSV files

    data_United_states = get_country_csv('UnitedStates')
    US_speechiness = data_United_states['speechiness']
    mean_us_speechiness = US_speechiness.mean()

    # Getting Indonesia data from CSV files

    data_Indonesia = get_country_csv('Indonesia')
    indo_speechiness = data_Indonesia['speechiness']
    mean_Indo_speechiness = indo_speechiness.mean()

    # Getting Brazil data from CSV files

    data_Brazil = get_country_csv('Brazil')
    brazil_speechiness = data_Brazil['speechiness']
    mean_Brazil_speechiness = brazil_speechiness.mean()

    # Getting Mexico data from CSV files

    data_Mexico = get_country_csv('Mexica')
    Mexico_speechiness = data_Mexico['speechiness']
    mean_Mexico_speechiness = Mexico_speechiness.mean()

    # Getting Japan data from CSV files

    data_Japan = get_country_csv('Japan')
    japan_speechiness = data_Japan['speechiness']
    mean_japan_speechiness = japan_speechiness.mean()

    # Declaring list of labels and mean values

    mesn_speechiness_list = [mean_us_speechiness, mean_Indo_speechiness, mean_Brazil_speechiness,
                             mean_Mexico_speechiness, mean_japan_speechiness]
    Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

    # Plotting the  graph of calculate data

    bar_plot = sns.barplot(x=Country_labels, y=mesn_speechiness_list, palette='deep')

    # Labelling the graph

    plt.title('Music Speechiness in Most Populated Countries')
    plt.xlabel('Country')
    plt.ylabel('speechiness')

    # Showing the data graph

    plt.show()



if __name__ == "__main__":

    liveness_graph()
    acousticness_graph()

    graph_danceabillity()
    graph_danca_vs_energy()
    graph_duration()
    graph_loudness()
    graph_speechiness()

    create_yearly_features_dotplot("danceability", "loudness")
    makeDanceabilityBarPlot("Australia", "UnitedStates")
    makeLoudnessBarplot("Australia", "UnitedStates")
    make_country_barplot("loudness")

    create_country_features_dotplot("loudness", "danceability", ["UnitedStates", "Spain", "Sweden", "NewZealand", "Mexica"])








