# Assessment #1: Perform data quality check by checking for missing values if any
# This script does the following:
# Loads the dataset into a pandas DataFrame.
# Prints basic information about the dataset using df.info().
# Checks for missing values in each column using df.isnull().sum().
# Prints the count of missing values for each column.
# Checks if there are any missing values in the entire dataset.
# Visualizes missing values using a heatmap.

import pandas as pd

# Load the 1688640705_hr_comma_sep.xlsx dataset into a pandas DataFrame
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

# Check for missing values in the dataset
missing_values = df.isnull().sum()

# Display the count of missing values for each column
print("\nMissing Values:")
print(missing_values)

# Check if there are any missing values in the entire dataset
if missing_values.sum() == 0:
    print("\nNo missing values found in the dataset.")
else:
    print("\nThere are missing values in the dataset.")

# Visualize missing values using a heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
plt.title('Missing Values Heatmap')
plt.show()

