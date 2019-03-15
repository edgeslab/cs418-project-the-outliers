import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def getCSV(country):
    return pd.read_csv('top50csv/' + country + "Top50.csv")


def makeDanceabilityBarPlot(countrya, countryb):
    countryAcsv = getCSV(countrya)
    countryBcsv = getCSV(countryb)
    sns.distplot(countryAcsv['danceability'], label=countrya + ' Danceability',)
    sns.distplot(countryBcsv['danceability'], label=countryb + ' Danceability')
    plt.title(countrya + ' VS ' + countryb + ' danceability')
    plt.xlabel('Danceability')
    plt.legend()
    plt.show()


def makeLoudnessBarplot(countrya, countryb):
    countryAcsv = getCSV(countrya)
    countryBcsv = getCSV(countryb)
    sns.distplot(countryAcsv['loudness'], label=countrya+' Loudness',)
    sns.distplot(countryBcsv['loudness'], label=countryb + ' Loudness')
    plt.title(countrya + ' VS ' + countryb + ' loudness')
    plt.xlabel('Loudness')
    plt.legend()
    plt.show()