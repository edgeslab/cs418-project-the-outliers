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

# Predict the closest year a playlist sounds like
def predict_playlist_year(playlist_id):
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "year")        # not using this test_data data
    data = spotify_api.get_playlist_audio_features(playlist_id)
    test_data = pd.io.json.json_normalize(data)

    # drop genres for yearly predictions bc we just wanna make our lives easier lol
    training_data = training_data.drop(['genre'], axis = 1)
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature', 'genre'], axis=1)

    svc = predict_svc(training_data, labels, test_data)
    return getClosestYear(svc)

def predict_playlist_genre(playlist_id):
    """
    Predicts what genres a playlist's songs sound like they belong to 
    Returns a dictionary d. d[genre_name] = song_count
    """

    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "genre")        # not using this test_data data
    data = spotify_api.get_playlist_audio_features(playlist_id)
    test_data = pd.io.json.json_normalize(data)

    # drop year for genre predictions
    training_data = training_data.drop(['year'], axis = 1)
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature', 'genre'], axis=1)

    rfc = predict_rfc(training_data, labels, test_data)

    genres = {}
    for g in rfc:
        if g not in genres:
            genres[g] = 0 
        genres[g] += 1

    return genres

# Predict a song's year
def predict_user_song_year(song_id):
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "year")        # not using this test data

    song_api_response = spotify_api.get_song_audio_features(song_id)
    test_data = pd.io.json.json_normalize(song_api_response)

    # drop genres for yearly predictions bc we just wanna make our lives easier lol
    training_data = training_data.drop(['genre'], axis = 1)
    # test_data = test_data.drop(['genre'], axis = 1) # we didn't add genre to get_song_audio_features() so this isnt needed rn
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type', 'time_signature'], axis=1)

    svc = predict_svc(training_data, labels, test_data)
    
    return getClosestYear(svc)

# Predict a song's genre
def predict_user_song_genre(song_id):
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "genre")      
    # get rid of year column
    training_data = training_data.drop(['year'], axis = 1)

    song_api_response = spotify_api.get_song_audio_features(song_id)
    test_data = pd.io.json.json_normalize(song_api_response)
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type', 'time_signature'], axis=1)

    # replace all genres with numbers
    genreMap = genreMapper(labels)
    for label in labels:
        label = genreMap[label]

    rfc = predict_rfc(training_data, labels, test_data)

    return rfc[0]

# Predict a year according to user provided features
def predict_user_diy_year(song_diy_features):
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "year")        # not using this test data
    training_data = training_data.drop(['genre', 'key', 'mode'], axis = 1)

    test_data = pd.io.json.json_normalize(song_diy_features)

    svc = predict_svc(training_data, labels, test_data)
    return getClosestYear(svc)

# Predict a song's genre according to user provided features
def predict_user_diy_genre(song_diy_features):
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, _, _ = getLabelsAndRemoveColumns(training_data, test_data, "genre")        # not using this test data
    training_data = training_data.drop(['year', 'key', 'mode'], axis = 1)

    test_data = pd.io.json.json_normalize(song_diy_features)

    rfc = predict_rfc(training_data, labels, test_data)
    
    genres = {}
    for g in rfc:
        if g not in genres:
            genres[g] = 0 
        genres[g] += 1

    return genres


def predictYear():
    # predict year for the 20% test data
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, _ = getLabelsAndRemoveColumns(training_data, test_data, "year")

    # drop genres for yearly predictions bc we just wanna make our lives easier lol
    training_data = training_data.drop(['genre'], axis = 1)
    test_data = test_data.drop(['genre'], axis = 1)

    # determined to have the best accuracy as compared to the other options
    svc_prediction = predict_svc(training_data, labels, test_data)
    year =  getClosestYear(svc_prediction)

    return svc_prediction, year

def genreMapper(labels):
    genreMap = {}
    counter = 0

    for label in labels:
        if label not in genreMap:
            genreMap[label] = counter
            counter = counter + 1
    
    return genreMap

def predictGenre():

    # predict genre for the 20% test data
    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, test_labels = getLabelsAndRemoveColumns(training_data, test_data, "genre")

    # replace all genres with numbers
    genreMap = genreMapper(labels)
    for label in labels:
        label = genreMap[label]

    # determined to have the best accuracy as compared to the other options
    rfc_prediction = predict_rfc(training_data, labels, test_data)

    return rfc_prediction

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

def getAccuracy(label):

    training_data, test_data = splitTrainAndTestData("topTracksYearsCSV/AllYearsTopTracks.csv")
    labels, training_data, test_data, test_labels = getLabelsAndRemoveColumns(training_data, test_data, label)

    rfc = predict_rfc(training_data, labels, test_data)
    dtc = predict_dtc(training_data, labels, test_data)
    svc = predict_svc(training_data, labels, test_data)
    lr = predict_lr(training_data, labels, test_data)

    prediction_accuracy(dtc, rfc, svc, lr, test_labels)

def prediction_accuracy(dtc, rfc, svc, lr, test_labels):
   
    #accuracy scores
    dtc_tree_acc = accuracy_score(dtc,test_labels)
    rfc_acc = accuracy_score(rfc,test_labels)
    l_acc = accuracy_score(lr,test_labels)
    s_acc = accuracy_score(svc,test_labels)

    classifiers = ['Decision Tree', 'Random Forest', 'Logistic Regression' , 'SVC']
    accuracy = np.array([dtc_tree_acc, rfc_acc, l_acc, s_acc])
    max_acc = np.argmax(accuracy)
    print('Decision Tree score: ', dtc_tree_acc)
    print('Random Forest score: ', rfc_acc)
    print('Support Vector score: ', s_acc )
    print('Logistic Regression score: ', l_acc )
    print(classifiers[max_acc] + ' is the best classifier for this problem')

def getYearlyFilenames():
    # get list of all files in years directory
    year_filenames = [] 
    for (path, names, filenames) in walk("topTracksYearsCSV/"):
        year_filenames.extend(filenames)
    year_filenames.remove("AllYearsTopTracks.csv")

    return year_filenames

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
    training_data = full_data[divider]
    test_data = full_data[~divider]  # not True

    return training_data, test_data

def getLabelsAndRemoveColumns(training_data, test_data, label_needed):
    """
    @label_needed is the column name that will be used as the label for classificatio
    Returns a list of labels for the training set and drops that column from both training and test data
    """
    labels = training_data[label_needed].tolist()
    training_data = training_data.drop(label_needed, axis=1)
    test_labels = test_data[label_needed]
    test_data = test_data.drop(label_needed, axis=1)

    return labels, training_data, test_data, test_labels

#TODO: get rid of main... it's only for testing purposes
if __name__ == "__main__":
    #prediction_list, year = predictYear()
    #print(prediction_list)

    #genre = predictGenre()
    genre = predict_playlist_genre('0Vg97p7M8sg62sQrFGiNkP')
    print(genre)

    #getAccuracy('genre')
