import pandas as pd

s = pd.Series([10, 20, 30])
v = pd.DataFrame([10, 20, 30])
# print(s)
# print(v)

#Series is 1D, dataframe is row column

marks = pd.Series(
    [88, 92, 75, 100],
    index=['Alice', 'Bob', 'Carol', 'David']
)

# print(marks)
# print(marks['Alice'])
# print(marks.iloc[0])
print(marks[(marks > 75) & (marks < 100)])


