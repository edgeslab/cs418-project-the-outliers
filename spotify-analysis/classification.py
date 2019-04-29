from os import walk

import pandas as pd
import numpy as np
import sklearn 
import scipy
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import spotify_api

def predict_playlist_year(playlist_id):
    training_data, labels = createTrainingData()
    data = spotify_api.get_playlist_audio_features(playlist_id)
    test_data = pd.io.json.json_normalize(data)
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature'], axis=1)

    print(test_data.shape)
    print(training_data.shape)
    rfc = predict_rfc(training_data, labels, test_data)
    return getClosestYear(rfc)

def predict_user_song_year(song_id):
    training_data, labels = createTrainingData()
    song_api_response = spotify_api.get_song_audio_features(song_id)
    test_data = pd.io.json.json_normalize(song_api_response)
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature'], axis=1)

    print(test_data.shape)
    print(training_data.shape)
    rfc = predict_rfc(training_data, labels, test_data)
    return getClosestYear(rfc)
    
def predictYear2():
    train, test = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, train, test = getLabelsAndRemoveColumns(train, test, "year")

    # determined to have the best accuracy as compared to the other options
    rfc_prediction = predict_rfc(train, labels, test)
    year =  getClosestYear(rfc_prediction)

    return rfc_prediction, year

def predictYear(filename):
    training_data, labels = createTrainingData()
    test_data = getTestData(filename)
    
    # determined to have the best accuracy as compared to the other options
    rfc_prediction = predict_rfc(training_data, labels, test_data)
    year =  getClosestYear(rfc_prediction)

    return rfc_prediction, year

def predict_rfc(training_data, labels, test_data):
    #RandomForestClassifier
    rfc_clf = RandomForestClassifier()
    rfc_clf.fit(training_data,labels)
    rfc_prediction = rfc_clf.predict(test_data)
    return rfc_prediction

def predict_dtc(training_data, labels, test_data):
    # DecisionTreeClassifier
    dtc_clf = tree.DecisionTreeClassifier()
    dtc_clf = dtc_clf.fit(training_data,labels)
    dtc_prediction = dtc_clf.predict(test_data)
    return dtc_prediction

def predict_svc(training_data, labels, test_data):
    # SupportVectorClassifier
    s_clf = SVC(kernel='linear')
    s_clf.fit(training_data, labels)
    s_prediction = s_clf.predict(test_data)
    return s_prediction

def predict_lr(training_data, labels, test_data):
    #LogisticRegression
    l_clf = LogisticRegression()
    l_clf.fit(training_data,labels)
    l_prediction = l_clf.predict(test_data)
    return l_prediction

def prediction_accuracy(dtc, rfc, svc, lr, test_labels):
    #accuracy scores

    dtc_tree_acc = accuracy_score(dtc,test_labels)
    rfc_acc = accuracy_score(rfc,test_labels)
    l_acc = accuracy_score(lr,test_labels)
    s_acc = accuracy_score(svc,test_labels)

    classifiers = ['Decision Tree', 'Random Forest', 'Logistic Regression' , 'SVC']
    accuracy = np.array([dtc_tree_acc, rfc_acc, l_acc, s_acc])
    max_acc = np.argmax(accuracy)
    print(classifiers[max_acc] + ' is the best classifier for this problem')

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
    training_data = pd.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'year'])

    for filename in year_filenames:
        data = pd.read_csv("topTracksYearsCSV/"+ filename) 
        data['year'] = filename[:4]
        training_data = training_data.append(data)

    labels = training_data['year'].tolist()

    # remove unneccessary columns
    training_data = training_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'type', 'year'], axis=1)

    return training_data, labels

def getTestData(filename):
    #TODO: make this actually get the real new user track... enter a url, get that playlist
    test_data = pd.read_csv("testPlaylistsCSV/" + filename + ".csv") 
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature'], axis=1)

    return test_data

def getClosestYear(results):
    """
    Finds the average from the results for the years in the results and returns the year that is closest
    to one of the available playlist years
    """
    sum = 0
    for year in results:
        sum = sum + int(year)
    avg = sum / len(results)

    year_files = getYearlyFilenames()
    years = []
    for file in year_files:
        years.append(file[:4])

    predicted_year = min(years, key=lambda x:abs(int(x)-avg))

    return predicted_year

def splitTrainAndTestData(filename): 
    """
    Cleans full data set
    Divides provided full data csv file randomly into ~80% training data and ~20% testing data
    """

    full_data = pd.read_csv(filename) 

    # remove unneccessary columns 
    full_data = full_data.drop(['Unnamed: 0', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'type'], axis=1)

    # gives a list of booleans the same length as the data
    divider = np.random.rand(len(full_data)) < 0.8  
    train = full_data[divider]
    test = full_data[~divider]  # not True

    return train, test

def getLabelsAndRemoveColumns(train, test, label_needed):
    """
    @label_needed is the column name that will be used as the label for classificatio
    Returns a list of labels for the training set and drops that column from both training and test data
    """

    labels = train[label_needed].tolist()
    train = train.drop(label_needed, axis=1)
    test = test.drop(label_needed, axis=1)

    return labels, train, test

#TODO: get rid of main... it's only for testing purposes
if __name__ == "__main__":
    #all_res, year = predictYear('2018TopTracks')

    res_prediction, year = predictYear2()
    print(year)