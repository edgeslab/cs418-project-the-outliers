import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# Retreiving US data from CSV files

data_United_states = pd.read_csv('UnitedStatesTop50.csv')
US_liveness = data_United_states['liveness']
mean_us_liveness = US_liveness.mean()

# Retreiving Indonesia data from CSV files

data_Indonesia = pd.read_csv('IndonesiaTop50.csv')
indo_liveness = data_Indonesia['liveness']
mean_Indo_liveness = indo_liveness.mean()

# Retreiving Brazil data from CSV files

data_Brazil = pd.read_csv('BrazilTop50.csv')
brazil_liveness = data_Brazil['liveness']
mean_Brazil_liveness = brazil_liveness.mean()


# Retreiving Mexico data from CSV files

data_Mexico = pd.read_csv('MexicaTop50.csv')
Mexico_liveness = data_Mexico['liveness']
mean_Mexico_liveness = Mexico_liveness.mean()

# Retreiving Japan data from CSV files

data_Japan = pd.read_csv('JapanTop50.csv')
japan_liveness = data_Japan['liveness']
mean_japan_liveness = japan_liveness.mean()

# Creating the list of mean values

mesn_liveness_list = [mean_us_liveness,mean_Indo_liveness,mean_Brazil_liveness,mean_Mexico_liveness,mean_japan_liveness]

# Declaring Labels for X axis

Country_labels = ['USA', 'Indonesia', 'Brazil', 'Mexico', 'Japan']

# Plotting the graph

bar_plot = sns.barplot(x=Country_labels, y= mesn_liveness_list,palette='deep')

# Labelling the Graph

plt.title('Music Liveness in Most Populated Countries in Spotify')
plt.xlabel('Country')
plt.ylabel('Liveness')

# Showing the Graph

plt.show()

