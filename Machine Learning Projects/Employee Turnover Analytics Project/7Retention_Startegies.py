# Assessment # 7: 7.	Suggest various retention strategies for targeted employees.
# 7.1. Using the best model, predict the probability of employee turnover in the test data.
# To determine the best-performing model, you can consider various metrics such as accuracy, precision, recall, and F1 score. Here's a summary of results:

# Logistic Regression:
# True Negative (TN) = 1718
# False Negative (FN) = 137
# True Positive (TP) = 577
# False Positive (FP) = 568
# Random Forest:
# True Negative (TN) = 2276
# False Negative (FN) = 15
# True Positive (TP) = 699
# False Positive (FP) = 10
# Gradient Boosting:
# True Negative (TN) = 2229
# False Negative (FN) = 48
# True Positive (TP) = 666
# False Positive (FP) = 57
# Now, let's calculate and compare some common classification metrics: 
# Definitions based on the given results
# Definitions based on the given results
logistic_regression = {'TN': 1718, 'FN': 137, 'TP': 577, 'FP': 568}
random_forest = {'TN': 2276, 'FN': 15, 'TP': 699, 'FP': 10}
gradient_boosting = {'TN': 2229, 'FN': 48, 'TP': 666, 'FP': 57}

# Calculate metrics
def calculate_metrics(results):
    accuracy = (results['TP'] + results['TN']) / (results['TP'] + results['TN'] + results['FP'] + results['FN'])
    precision = results['TP'] / (results['TP'] + results['FP'])
    recall = results['TP'] / (results['TP'] + results['FN'])
    f1_score = 2 * precision * recall / (precision + recall)
    return accuracy, precision, recall, f1_score

# Calculate metrics for each model
lr_metrics = calculate_metrics(logistic_regression)
rf_metrics = calculate_metrics(random_forest)
gb_metrics = calculate_metrics(gradient_boosting)

# Format and print the results
print(f"{'Model':<20}{'Accuracy':<15}{'Precision':<15}{'Recall':<15}{'F1 Score':<15}")
print(f"{'Logistic Regression':<20}{lr_metrics[0]:<15.4f}{lr_metrics[1]:<15.4f}{lr_metrics[2]:<15.4f}{lr_metrics[3]:<15.4f}")
print(f"{'Random Forest':<20}{rf_metrics[0]:<15.4f}{rf_metrics[1]:<15.4f}{rf_metrics[2]:<15.4f}{rf_metrics[3]:<15.4f}")
print(f"{'Gradient Boosting':<20}{gb_metrics[0]:<15.4f}{gb_metrics[1]:<15.4f}{gb_metrics[2]:<15.4f}{gb_metrics[3]:<15.4f}")

# Overall Performance: for overall classification performance, accuracy is a useful metric. Random Forest has the highest accuracy (0.9917). Based on these considerations, Random Forest seems to perform exceptionally well across multiple metrics in this scenario. 
# Predict the probability of employee turnover in the test data (Using Random Forest).

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the 1688640705_hr_comma_sep.xlsx dataset into a pandas DataFrame
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Select features and target variable
X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years']]
y = df['left']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier model
rf_model = RandomForestClassifier(random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Predict the probability of employee turnover on the test data
probabilities = rf_model.predict_proba(X_test)[:, 1]

# Display the predicted probabilities
print("Predicted Probabilities of Employee Turnover:")
print(probabilities)

# 7.2.	Based on the below probability score range, categorize the employees into four zones and suggest your thoughts on the retention strategies for each zone.
# (1) Safe Zone (Green) (Score < 20%)
# (2) Low Risk Zone (Yellow) (20% < Score < 60%)
# (3) Medium Risk Zone (Orange) (60% < Score < 90%)
# (4) High Risk Zone (Red) (Score > 90%).

# Select features and target variable
X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years']]
y = df['left']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier model
rf_model = RandomForestClassifier(random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Predict the probability of employee turnover on the test data
probabilities = rf_model.predict_proba(X_test)[:, 1]

# Define probability score ranges for each zone
safe_zone = 0.20  # 20%
low_risk_zone = 0.60  # 60%
medium_risk_zone = 0.90  # 90%

# Categorize employees into zones
employee_zones = []
for probability in probabilities:
    if probability < safe_zone:
        employee_zones.append("Safe Zone (Green)")
    elif safe_zone <= probability < low_risk_zone:
        employee_zones.append("Low Risk Zone (Yellow)")
    elif low_risk_zone <= probability < medium_risk_zone:
        employee_zones.append("Medium Risk Zone (Orange)")
    else:
        employee_zones.append("High Risk Zone (Red)")

# Add the 'employee_zones' information to the DataFrame
df_test = df.loc[X_test.index]  # Use the index of the test set
df_test['Employee Zone'] = employee_zones

# Display the DataFrame with Zone information
print("Employee Data with Zones:")
print(df_test[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'left', 'Employee Zone']])

# Suggestions:
# Safe Zone (Green):
# Recognize and appreciate employees' contributions regularly.
# Provide opportunities for skill development and career growth.
# Foster a positive work environment with work-life balance initiatives.
# Encourage teamwork and collaboration among employees.

# Low Risk Zone (Yellow):
# Conduct regular check-ins to assess job satisfaction and address concerns.
# Offer additional training programs to enhance skills and productivity.
# Provide opportunities for employees to take on leadership roles in projects.
# Implement flexible work arrangements to accommodate personal needs.

# Medium Risk Zone (Orange):
# Conduct in-depth performance reviews and address any concerns proactively.
# Offer mentorship programs to provide guidance and support.
# Introduce employee engagement activities to boost morale.
# Implement targeted retention bonuses or incentives for key contributors.

# High Risk Zone (Red):
# Conduct exit interviews to understand reasons for dissatisfaction.
# Implement immediate interventions to address specific concerns.
# Consider tailored retention packages for critical employees.
# Develop a strategic plan for knowledge transfer in case of departure.

# These strategies are general recommendations and may need to be adjusted based on the specific needs and dynamics of the organization. Additionally, regular communication and feedback from employees in each zone can provide valuable insights for refining and adapting the retention strategies over time.