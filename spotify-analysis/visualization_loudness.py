import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Loudness Comparison Example
AustraliaTop50_csv = pd.read_csv('ArgentinaTop50.csv')
USATop50_csv = pd.read_csv('UnitedStatesTop50.csv')

Australia_Loudness = AustraliaTop50_csv['loudness']
USA_Loudness = USATop50_csv['loudness']

sns.distplot(AustraliaTop50_csv['loudness'],label='Australia Loudness',)
sns.distplot(USATop50_csv['loudness'],label= 'USA Loudness')
plt.title ('Australia VS USA Looudness')
plt.xlabel('Loudness')
plt.legend()
plt.show()


