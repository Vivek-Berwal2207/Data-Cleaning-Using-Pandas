import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Name' : ['Alice', 'Alice', None, 'David', 'Eve'],
    'Age'  : [22, 22, 23, 21, None],
    'Score': [88, 88, np.nan, 100, 65]
})
print(df)
# print(df.isnull().sum())

#2. Drop rows with ANY null
# df_clean = df.dropna()
# print(df_clean)

#3. Drop only if ALL values in the row are null
# df_clean = df.dropna(how='all')
# print(df_clean)

#4. Fill with a fixed value
# df['Score'].fillna(0, inplace=True)
# print(df)

# df['Age'].fillna(df['Age'].mean(), inplace=True)
# print(df)

#Find duplicates
# print(df.duplicated().sum())
# print(df[df.duplicated()])



#Drop duplicates (keeps first occurrence)
# df.drop_duplicates(inplace=True)
# print(df)

#Drop duplicates based on specific columns only
df.drop_duplicates(subset=['Name', 'Age'], keep='first', inplace=True)
print(df)