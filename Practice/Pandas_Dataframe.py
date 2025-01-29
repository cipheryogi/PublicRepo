import pandas as pd

Table = {'Name': ['Birdie', 'Num1', 'Num2'], 'Age': [30, 40, 50], 'country': ['India', 'USA', 'Canada']}
Table1 = {'Name': ['Birdie', 'Num1', 'Num2'], 'Education': ['B.Tech', 'B.Sc', 'M.Tech'], 'Gender': ['Male', 'Female'], 'Preference': ['Non-veg', 'Veg', 'Omni']}

data = pd.DataFrame(Table)
data1 = pd.DataFrame(Table1)

print('Type of data: ', type(data))  # dataframe
print('Shape of data: ', data.shape)  # 3 X 3 matrix
print(data)

# Merge the DataFrames on the 'Name' column, which is common between both DataFrames
result = data.merge(data1, on='Name', how='inner')
print(result)

# Merge the DataFrames on the 'Name' column, which is common between both DataFrames
# result = data.merge(data1, on='Name', how='inner')
# print(result)


