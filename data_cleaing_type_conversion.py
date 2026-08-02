import pandas as pd

df = pd.DataFrame({
    'Date'    : ['2024-01-15', '2024-02-20', '2024-03-05'],
    'Sales'   : ['1500.50', '2000.00', '1750.25'],
    'Category': ['A', 'B', 'A']
})
print(df)

# df['Sales'] = pd.to_numeric(df['Sales'])
# print(df)

df['Date'] = pd.to_datetime(df['Date'])
#print(df)

#Extract date parts
df['Year']  = df['Date'].dt.year
df['Month']  = df['Date'].dt.month
df['Day']  = df['Date'].dt.day

df['Weekday'] = df['Date'].dt.day_name()
print(df)