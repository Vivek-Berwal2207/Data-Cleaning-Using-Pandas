import pandas as pd
import numpy as np
hr_data = pd.DataFrame({
    'Emp_ID': [101, 102, 101, 103, 104, None, 105],
    'Name': ['Liam', 'Noah', 'Liam', 'Oliver', 'Emma', None, 'Ava'],
    'Department': ['Sales', 'Engineering', 'Sales', None, 'HR', None, 'Marketing'],
    'Monthly_Salary': [5000, 6200, 5000, 4800, np.nan, None, 5400],
    'Bonus_Pct': [0.10, np.nan, 0.10, 0.05, 0.12, None, np.nan]
})

print(hr_data)

# print("Task1: Remove rows where all columns contain missing values.")
# hr_data.dropna(how='all', inplace=True)
# print(hr_data)

# print("Task2: Locate and purge duplicate rows based on the combinations of Emp_ID and Name, keeping only the first occurrence.")
# hr_data['duplicate_data'] = hr_data.duplicated(
#     subset=["Emp_ID", "Name"], keep='first')
# print(hr_data)
# hr_data = hr_data.drop_duplicates(subset=["Emp_ID", "Name"], keep='first')
# print(hr_data)

# print("Calculate the mean value of the remaining values in Monthly_Salary and fill any missing data points inside that column with it.")
# monthly_sal_mean = hr_data["Monthly_Salary"].mean()
# hr_data["Monthly_Salary"] = hr_data["Monthly_Salary"].fillna(monthly_sal_mean)
# print(hr_data)

# print("Replace any remaining null values inside the Bonus_Pct column with a hardcoded static float value of 0.00.")
# hr_data["Bonus_Pct"] = hr_data["Bonus_Pct"].fillna(0.00)
# print(hr_data)
