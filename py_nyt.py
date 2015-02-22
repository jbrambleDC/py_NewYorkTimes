import csv
import pandas as pd
from ggplot import *

#GET DATA
df = pd.read_csv('doing_data_science/dds_datasets/nyt1.csv')
labels = ["{0} - {1}".format(i,i+4) for i in range(0,100,5)]
df['age_group'] = pd.cut(df.Age, range(0,105,5), right=False, labels = labels)
groups = df.groupby('age_group').groups
for i,k in groups.items():
    print i,len(k)
p = ggplot(aes(x= 'age_group',y='Impressions', fill='age_group'), data=df)
p + geom_histogram()
print p

