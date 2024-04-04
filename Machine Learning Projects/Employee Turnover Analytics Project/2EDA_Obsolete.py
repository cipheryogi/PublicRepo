# Assessment # 2: Understand what factors contributed most to employee turnover by EDA
# Exploratory Data Analysis (EDA) is a crucial step in understanding what factors contribute most to employee turnover. In Python, we can use various libraries such as pandas, matplotlib, seaborn, and others for EDA. Here's the analysis:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step1: Load the employee turnover dataset

df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Display basic information about the dataset
print(df.info())

# End of Step1.

# Step2: Explore the data to understand its structure, features, and basic statistics. And visualize the data.

# Display the first few rows of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# Distribution of target variable (turnover) with legend
plt.figure(figsize=(8, 5))
sns.countplot(x='left', data=df, hue='left', palette={0: 'blue', 1: 'orange'})
plt.title('Employee Turnover Distribution')
plt.legend(title='Turnover', labels=['Not Left', 'Left'])
plt.show()

# Pairplot to visualize relationships between numerical features
sns.pairplot(df, hue='left')
plt.show()

# Correlation matrix to identify relationships between numerical features
# Identify and exclude non-numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
numeric_df = df[numeric_columns]

# Correlation matrix to identify relationships between numerical features
correlation_matrix = numeric_df.corr()

# Check if there are non-trivial correlations
if not correlation_matrix.empty:
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
else:
    print("No non-trivial correlations found.")

# Explore the relationship between features and turnover using barplots
# Define colors for the bar charts
colors = sns.color_palette("pastel")

# Explore the relationship between features and turnover using barplots with legends and colors
for column in ['number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'sales', 'salary']:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='left', data=df, palette=colors)
    plt.title(f'{column} vs Turnover')
    plt.xlabel(column)
    plt.ylabel('Turnover')
    plt.show()

# End of Step2.

# Step3: Identify key factors that contribute to turnover by analyzing relationships and patterns in the data.
# Feature Importance: Use machine learning models or statistical tests to determine the importance of each feature.
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assume 'left' is the target variable
X = df.drop('left', axis=1)
y = df['left']

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X, columns=['sales', 'salary'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}") 
# Note: Accuracy is 0.988 after executing this code. An accuracy of 0.988 means that the model correctly predicted the turnover status for approximately 98.8% of the instances in your test data.

# End of Step3.

# Step4: Deep dive into factors. Explore key factors in more detail by creating specific visualizations or conducting further statistical analysis.
# Boxplot to compare a numerical feature with turnover
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

X = df.drop('left', axis=1)
y = df['left']

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X, columns=['sales', 'salary'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")

# The output of Step4 above is: 
# Accuracy: 0.9886666666666667
# Precision: 0.9869565217391304
# Recall: 0.9645892351274787
# F1-Score: 0.9756446991404011

# End of Step4.

# Step5: Perform hypothesis testing and validate the observations.
from scipy.stats import ttest_ind

# Assume 'left' is the target variable
turnover_yes = df[df['left'] == 1]
turnover_no = df[df['left'] == 0]

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    t_stat, p_value = ttest_ind(turnover_yes[column], turnover_no[column])
    print(f"T-statistic for {column}: {t_stat}, p-value: {p_value}")





