import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Danceability Comparison Example
AustraliaTop50CSV = pd.read_csv('ArgentinaTop50.csv')
USATop50csv = pd.read_csv('UnitedStatesTop50.csv')

AustraliaDanceability = AustraliaTop50CSV['danceability']
USADanceability = USATop50csv['danceability']
#sns.barplot("danceability",data=AustraliaTop50CSV)
#sns.barplot("danceability",data=USATop50csv)
sns.distplot(AustraliaTop50CSV['danceability'],label='Australia Danceability',)
sns.distplot(USATop50csv['danceability'],label= 'USA Danceability')
plt.title ('Australia VS USA danceability')
plt.xlabel('Danceability')
plt.legend()
plt.show()


