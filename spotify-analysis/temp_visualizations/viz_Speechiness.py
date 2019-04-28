import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt


# Getting US data from CSV files


data_United_states = pd.read_csv('UnitedStatesTop50.csv')
US_speechiness = data_United_states['speechiness']
mean_us_speechiness = US_speechiness.mean()

# Getting Indonesia data from CSV files


data_Indonesia = pd.read_csv('IndonesiaTop50.csv')
indo_speechiness = data_Indonesia['speechiness']
mean_Indo_speechiness = indo_speechiness.mean()

# Getting Brazil data from CSV files


data_Brazil = pd.read_csv('BrazilTop50.csv')
brazil_speechiness = data_Brazil['speechiness']
mean_Brazil_speechiness = brazil_speechiness.mean()

# Getting Mexico data from CSV files


data_Mexico = pd.read_csv('MexicaTop50.csv')
Mexico_speechiness = data_Mexico['speechiness']
mean_Mexico_speechiness = Mexico_speechiness.mean()

# Getting Japan data from CSV files


data_Japan = pd.read_csv('JapanTop50.csv')
japan_speechiness = data_Japan['speechiness']
mean_japan_speechiness = japan_speechiness.mean()

# Declaring list of labels and mean values

mesn_speechiness_list = [mean_us_speechiness,mean_Indo_speechiness,mean_Brazil_speechiness,mean_Mexico_speechiness,mean_japan_speechiness]
Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

# Plotting the  graph of calculate data

bar_plot = sns.barplot(x=Country_labels, y= mesn_speechiness_list,palette='deep')

# Labelling the graph

plt.title('Music Speechiness in Most Populated Countries')
plt.xlabel('Country')
plt.ylabel('speechiness')

# Showing the data graph

plt.show()

