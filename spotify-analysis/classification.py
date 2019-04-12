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


def predictYear(filename, year):
    training_data, labels = createTrainingData()
    test_data = getTestData(filename)
    
    rfc = predict_rfc(training_data, labels, test_data)


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
    test_data = pd.read_csv("topTracksYearsCSV/" + filename + ".csv") 
    test_data = test_data.drop(['id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'type','time_signature'], axis=1)

    return test_data

#TODO: get rid of main... it's only for testing purposes
if __name__ == "__main__":
    predictYear('2017TopTracks', '2017')