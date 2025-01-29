# Assessment # 2: Understand what factors contributed most to employee turnover by EDA
# 2.1.	Draw a heatmap of the Correlation Matrix between all numerical features/columns in the data.
# To draw a heatmap of the correlation matrix between numerical features in Python, we can use the seaborn library along with matplotlib for visualization. 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Extract numerical features
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numerical_features.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# 2.2.	Draw the distribution plot of 
# ■	Employee Satisfaction (use column satisfaction_level)
# ■	Employee Evaluation (use column last_evaluation)
# ■	Employee Average Monthly Hours (use column average_montly_hours)

# Set up the figure with subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Plot distribution of Employee Satisfaction
sns.histplot(df['satisfaction_level'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Employee Satisfaction')
axes[0].set_xlabel('Satisfaction Level')

# Plot distribution of Employee Evaluation
sns.histplot(df['last_evaluation'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Employee Evaluation')
axes[1].set_xlabel('Evaluation Level')

# Plot distribution of Average Monthly Hours
sns.histplot(df['average_montly_hours'], kde=True, ax=axes[2], color='green')
axes[2].set_title('Average Monthly Hours')
axes[2].set_xlabel('Hours')

# Adjust layout
plt.tight_layout()
plt.show()

# 2.3.	Draw the bar plot of Employee Project Count of both employees who left and who stayed in the organization (use column number_project and hue column left)  and give your inferences from the plot.

# Set up the figure
plt.figure(figsize=(8, 6))

# Plot bar plot of Employee Project Count with hue based on 'left'
sns.countplot(x='number_project', hue='left', data=df, palette='viridis')

# Set plot labels and title
plt.title('Employee Project Count by Left Status')
plt.xlabel('Number of Projects')
plt.ylabel('Count')

# Show the plot. sns.countplot is used to create a bar plot, with the x-axis representing the number of projects (number_project) and differentiating between employees who left (left=1) and those who stayed (left=0).
plt.show()

# Inference: 
# The bar plot shows the distribution of the number of projects for employees who left and employees who stayed. From the bar plot its apparent that employees who are involved in 3 to 5 projects are likely stay with the company while the employees who are involved in less than 3 or more than 5 projects are likely to leave the company.



