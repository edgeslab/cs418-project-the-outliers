import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# Getting the US data data from CSV files

data_United_states = pd.read_csv('UnitedStatesTop50.csv')
US_acousticness = data_United_states['acousticness']
mean_us_acousticness = US_acousticness.mean()

# Getting the Indonesia data from CSV files

data_Indonesia = pd.read_csv('IndonesiaTop50.csv')
indo_acousticness = data_Indonesia['acousticness']
mean_Indo_acousticness = indo_acousticness.mean()

# Getting the Brazil data from CSV files


data_Brazil = pd.read_csv('BrazilTop50.csv')
brazil_acousticness = data_Brazil['acousticness']
mean_Brazil_acousticness = brazil_acousticness.mean()

# Getting the Mexico data from CSV files


data_Mexico = pd.read_csv('MexicaTop50.csv')
Mexico_acousticness = data_Mexico['acousticness']
mean_Mexico_acousticness = Mexico_acousticness.mean()

# Getting the Japan data data from CSV files


data_Japan = pd.read_csv('JapanTop50.csv')
japan_acousticness = data_Japan['acousticness']
mean_japan_acousticness = japan_acousticness.mean()

# Ca;culating mean and puttong it into list

mesn_acousticness_list = [mean_us_acousticness,mean_Indo_acousticness,mean_Brazil_acousticness,mean_Mexico_acousticness,mean_japan_acousticness]

# Creating the labels for X axis

Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

# Plotting the Graph

bar_plot = sns.barplot(x=Country_labels, y= mesn_acousticness_list,palette='deep')

# Labelling the Graph

plt.title('Music Acousticness in Most Populated Countries in Spotify')
plt.xlabel('Country')
plt.ylabel('Acousticness')

# Showing the Graph

plt.show()

