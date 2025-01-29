# Assessment # 3: Perform clustering of Employees who left based on their satisfaction and evaluation.
# 3.1.	Choose columns satisfaction_level, last_evaluation and left.
# 3.2.	Do KMeans clustering of employees who left the company into 3 clusters.
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Select relevant columns for clustering
columns_for_clustering = ['satisfaction_level', 'last_evaluation']

# Filter rows for employees who left
left_employees_df = df[df['left'] == 1]

# Extract features for clustering
X = left_employees_df[columns_for_clustering]

# Perform KMeans clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
left_employees_df['cluster'] = kmeans.fit_predict(X)

# Display the resulting clusters
print(left_employees_df[['satisfaction_level', 'last_evaluation', 'cluster']])

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(left_employees_df['satisfaction_level'], left_employees_df['last_evaluation'], c=left_employees_df['cluster'], cmap='viridis')
plt.title('KMeans Clustering of Employees Who Left')
plt.xlabel('Satisfaction Level')
plt.ylabel('Last Evaluation')
plt.show()

# 3.3.Based on the satisfaction and evaluation factors, give your thoughts on the employee clusters.
# Inference: From the scatter plot it can be inferred that the employees who received higher rating between 0.8 to 1.0, have shown greater employee satisfaction (0.8)

