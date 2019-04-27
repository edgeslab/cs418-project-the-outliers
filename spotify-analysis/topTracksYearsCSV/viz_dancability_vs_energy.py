import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# Retreiving the data from CSV files

data2010 = pd.read_csv('2010TopTracks.csv')
energy2010 = data2010['energy']
data2011 = pd.read_csv('2011TopTracks.csv')
energy2011 = data2011['energy']
data2012 = pd.read_csv('2012TopTracks.csv')
energy2012 = data2012['energy']
data2013 = pd.read_csv('2013TopTracks.csv')
energy2013 = data2013['energy']
data2014 = pd.read_csv('2014TopTracks.csv')
energy2014 = data2014['energy']
data2015= pd.read_csv('2015TopTracks.csv')
energy2015 = data2015['energy']
data2016 = pd.read_csv('2016TopTracks.csv')
energy2016 = data2016['energy']
data2017 = pd.read_csv('2017TopTracks.csv')
energy2017 = data2017['energy']
data2018 = pd.read_csv('2018TopTracks.csv')
energy2018 = data2018['energy']

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


#making the list of mean values of danceability and energy from the data




lisy = [danca2010.mean(), danca2011.mean(), danca2012.mean(), danca2013.mean(), danca2014.mean(), danca2015.mean(), danca2016.mean(), danca2017.mean(), danca2018.mean()]
list_Energy = [energy2010.mean(), energy2011.mean(), energy2012.mean(), energy2013.mean(), energy2014.mean(), energy2015.mean(), energy2016.mean(), energy2017.mean(), energy2018.mean()]

#Labelling X Axis

year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

#plotting thr graphs

plot1 = sns.pointplot(x = year_labels, y=lisy, label ='Danceability', color='purple')
plot2 = sns.pointplot(x = year_labels, y= list_Energy, label ='Energy', color='green')

# Labelling the graphs

plt.title('Danceability VS Energy of Top Songs From 2010-2018')
plt.xlabel('Year')
plt.ylabel('Danceability / Energy')
plot1.legend(labels = ['Danceability','Energy'],loc = 'upper left', ncol = 2)

#Showing the graph

plt.show()

