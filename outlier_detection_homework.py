#Homework
# marks = [70, 75, 80, 85, 90, 300]
# salary = [25000, 28000, 30000, 27000, 29000, 500000]
# ages = [21, 22, 20, 23, 24, 150]
#scores = [72, 78, 80, 85, -20]

import pandas as pd
import numpy as np

# marks = pd.Series([70, 75, 80, 85, 90, 300])
# z_scores = ( marks - marks.mean()) / marks.std()
# z_outlier = marks[abs(z_scores) > 2]
# print('Z-score outliers:', z_outlier.values)

# salary = pd.Series([25000, 28000, 30000, 27000, 29000, 500000])
# z_scores = (salary - salary.mean()) / salary.std()
# z_outliers = salary[abs(z_scores) > 2]
# print('Z-score outliers:', z_outliers.values)

# ages = pd.Series([21, 22, 20, 23, 24, 150])
# z_scores = (ages - ages.mean()) / ages.std()
# z_outliers = ages[abs(z_scores) > 2]
# print('z outliers:', z_outliers.values)

scores = pd.Series([72, 78, 80, 85, -20])
z_scores = (scores - scores.mean()) / scores.std()
z_outliers = scores[abs(z_scores) > 2]
print('z outliers:', z_outliers.values)
#need to check this negative wala