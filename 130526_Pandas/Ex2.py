import pandas as pd
import numpy as np
#From a dictionary
data = {
    'Name'    : ['Alice','Bob','Carol','David','Eve'],
    'Age'     : [22, 25, 23, 21, 24],
    'Score'   : [88, 92, 75, 100, 65],
    'Grade'   : ['B','A','C','A','F'],
    'City'    : ['Mumbai','Delhi','Bangalore','Mumbai','Chennai']
}

df = pd.DataFrame(data)
#print(df.head(4))   #first 5 rows
# print(df.tail(3))   #last 3 rows
# print(df.shape)     #size of mattrix
# print(df.columns)
# print(df.dtypes)
# print(df.info())
#print(df.describe())
#print(df.isnull().sum())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# print(df[['Name', 'City']])
print(df.iloc[1:3])
print(df.iloc[1,3])

print(df[(df['Grade'] == 'A') & (df['Age'] < 24)])
print(df[df['City'].isin(['Delhi', 'Bangalore', 'ABC'])])