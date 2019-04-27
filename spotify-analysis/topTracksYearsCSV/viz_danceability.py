import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# Getting the data from the CSV files

data2010 = pd.read_csv('2010TopTracks.csv')
danca2010 = data2010['danceability']
data2011 = pd.read_csv('2011TopTracks.csv')
danca2011 = data2011['danceability']
data2012 = pd.read_csv('2012TopTracks.csv')
danca2012 = data2012['danceability']
data2013 = pd.read_csv('2013TopTracks.csv')
danca2013 = data2013['danceability']
data2014 = pd.read_csv('2014TopTracks.csv')
danca2014 = data2014['danceability']
data2015= pd.read_csv('2015TopTracks.csv')
danca2015 = data2015['danceability']
data2016 = pd.read_csv('2016TopTracks.csv')
danca2016 = data2016['danceability']
data2017 = pd.read_csv('2017TopTracks.csv')
danca2017 = data2017['danceability']
data2018 = pd.read_csv('2018TopTracks.csv')
danca2018 = data2018['danceability']

# making a list of mean values of danceability of different countries

lisy = [danca2010.mean(),danca2011.mean(),danca2012.mean(),danca2013.mean(),danca2014.mean(),danca2015.mean(),danca2016.mean(),danca2017.mean(),danca2018.mean()]

# making list of year labels

year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

#plotting the graph

plot = sns.pointplot(x = year_labels, y=lisy, label="Loudness", linestyle="-")

# labelling the graph

plt.title('Danceability of Top Songs From 2010-2018')
plt.xlabel('Year')
plt.ylabel('Danceability')
plot.legend(['Danceability'])

#showing the graph

plt.show()