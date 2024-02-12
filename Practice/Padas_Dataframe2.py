import pandas as pd

df1 = pd.read_csv('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Data Science with Python/Superstore.csv')
# print all data
# print(df1)
# first 5 rows
print(df1.head()) 
# last 5 rows. Note: 'NaN' means the data is missing in that particular field.
print(df1.tail()) 
# all info about the data. Note that 'string' is shown as 'Object' data type
print(df1.info()) 
# check the missing values 
print(df1.isnull().sum())
# check the missing values  - alternate function
print(df1.isna().sum())
# drop the missing values - excludes the entire row even if any one of the fields in NaN
print(df1.dropna())
# drop the missing values - update the values stored in df1 variable permanently.
print(df1.dropna(inplace=True))