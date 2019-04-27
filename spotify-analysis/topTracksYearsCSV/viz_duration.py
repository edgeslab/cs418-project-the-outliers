import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# Getting data from CSV files

data2010 = pd.read_csv('2010TopTracks.csv')
duration_2010 = data2010['duration_ms']
data2011 = pd.read_csv('2011TopTracks.csv')
duration_2011 = data2011['duration_ms']
data2012 = pd.read_csv('2012TopTracks.csv')
duration_2012 = data2012['duration_ms']
data2013 = pd.read_csv('2013TopTracks.csv')
duration_2013 = data2013['duration_ms']
data2014 = pd.read_csv('2014TopTracks.csv')
duration_2014 = data2014['duration_ms']
data2015= pd.read_csv('2015TopTracks.csv')
duration_2015 = data2015['duration_ms']
data2016 = pd.read_csv('2016TopTracks.csv')
duration_2016 = data2016['duration_ms']
data2017 = pd.read_csv('2017TopTracks.csv')
duration_2017 = data2017['duration_ms']
data2018 = pd.read_csv('2018TopTracks.csv')
duration_2018 = data2018['duration_ms']

# Making list of mean values of duration for consecutive years


lisy = [duration_2010.mean(),duration_2011.mean(),duration_2012.mean(),duration_2013.mean(),duration_2014.mean(),duration_2015.mean(),duration_2016.mean(),duration_2017.mean(),duration_2018.mean()]

# Label list for x Axis

year_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

# Putting up title and labels

plt.title('Duration of Top Songs From 2010-2018')
plt.xlabel('Year')
plt.ylabel('Duration in milisconds')

# Plotting the graph

sns.pointplot(x = year_labels, y=lisy, color='purple')

#Showing the Graph

plt.show()

