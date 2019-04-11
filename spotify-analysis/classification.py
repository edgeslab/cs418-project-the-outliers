from os import walk

import pandas as pd
import numpy as np

import sklearn 
import scipy
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer

def predictYear():
    training_data, labels = createTrainingData()
    test_data = getTestData()

    #vectorizer = TfidfVectorizer()
    #vectorizer.fit(training_data['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type'])
    #training_data = vectorizer.transform(training_data['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type'])
    #test_data = vectorizer.transform(test_data['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type'])

    # so, this not working right now
    # TODO: i believe we have to do what we did for the homework and make a vectorizor to make it a sparse array?
    s_clf = SVC()
    s_clf.fit(training_data, labels)
    s_prediction = s_clf.predict(test_data)
    print(s_prediction)


def getYearlyFilenames():
    # get list of all files in years directory
    year_filenames = [] 
    for (path, names, filenames) in walk("topTracksYearsCSV/"):
        year_filenames.extend(filenames)
    return year_filenames

def createTrainingData():
    year_filenames = getYearlyFilenames()

    # empty data frame with all column names... 
    # is there a way to get the column names without writing them out manually lol?
    training_data = pd.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'year'])

    for filename in year_filenames:
        data = pd.read_csv("topTracksYearsCSV/"+ filename) 
        data['year'] = filename[:4]
        training_data = training_data.append(data)

    labels = training_data['year'].tolist()

    # remove unneccessary columns
    training_data = training_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'year'], axis=1)

    return training_data, labels

def getTestData():
    #TODO: make this actually get the real new user track... enter a url, get that playlist
    test_data = pd.read_csv("topTracksYearsCSV/2017TopTracks.csv") 
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'], axis=1)

    return test_data

#TODO: get rid of main... it's only for testing purposes
if __name__ == "__main__":
    predictYear()