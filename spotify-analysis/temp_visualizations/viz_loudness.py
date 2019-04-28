import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# CSV file data accquisition of US

data_United_states = pd.read_csv('UnitedStatesTop50.csv')
US_loudness = data_United_states['loudness']
mean_us_loudness = US_loudness.mean()

# CSV file data accquisition of Indonesia


data_Indonesia = pd.read_csv('IndonesiaTop50.csv')
indo_loudness = data_Indonesia['loudness']
mean_Indo_loudness = indo_loudness.mean()

# CSV file data accquisition of Brazil


data_Brazil = pd.read_csv('BrazilTop50.csv')
brazil_loudness = data_Brazil['loudness']
mean_Brazil_loudness = brazil_loudness.mean()

# CSV file data accquisition of Mexico


data_Mexico = pd.read_csv('MexicaTop50.csv')
Mexico_loudness = data_Mexico['loudness']
mean_Mexico_loudness = Mexico_loudness.mean()

# CSV file data accquisition of Jaopan


data_Japan = pd.read_csv('JapanTop50.csv')
japan_loudness = data_Japan['loudness']
mean_japan_loudness = japan_loudness.mean()

# Creating labels and calculating mean valeus

mesn_loudness_list = [mean_us_loudness,mean_Indo_loudness,mean_Brazil_loudness,mean_Mexico_loudness,mean_japan_loudness]
Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

# Plotting the barplot

bar_plot = sns.barplot(x=Country_labels, y= mesn_loudness_list,palette='deep')

# Puttom=ng up title and labels for graph

plt.title('Music Loudness in Most Populated Countries in Spotify')
plt.xlabel('Country')
plt.ylabel('Loudness')

# Showing the graph

plt.show()