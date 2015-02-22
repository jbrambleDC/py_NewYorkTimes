import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ggplot import *

plt.style.use("ggplot")

#GET DATA
df = pd.read_csv('doing_data_science/dds_datasets/nyt1.csv')
#R-tastic way of labeling
#labels = ["{0} - {1}".format(i,i+4) for i in range(0,100,5)]
#df['age_group'] = pd.cut(df.Age, range(0,105,5), right=False, labels = labels)
#pythonic way
age_range = [0, 19, 25, 35, 45, 55, 65, np.inf]
age_labels = ['18--', '18-24', '25-34', '35-44', '45-54', '55-64', '65++']
df['Age_group'] = pd.cut(df['Age'], bins=age_range, right=False, labels=age_labels)
#Plot Click Through Rate and Impressions
#first clicks and impressions
print "Data Frame Grouped by Clicks and Impressions per Age Group:"
print df.groupby('Age_group')[['Impressions','Clicks']].sum()
grouped = df.groupby('Age_group')[['Impressions','Clicks']].sum()
grouped['CTR'] = grouped['Clicks']/grouped['Impressions']
print grouped['CTR']
grouped[['Impressions', 'CTR']].plot(kind='bar', subplots=True)
#uncomment line below to show plot
plt.show()
#lets define a new variable to segment users on click behavior. And some additional EDA
df['Gender'] = df['Gender'].apply(lambda x: 'male' if x else 'female')
print df.describe()
print df.groupby(['Age_group', 'Gender'])[['Impressions','Clicks']].sum()
print df.groupby('Age_group')['Age'].agg([len,  np.min, np.mean, np.max])
