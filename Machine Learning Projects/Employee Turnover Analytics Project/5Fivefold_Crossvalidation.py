import pandas as pd
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Features and target variable
X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years']]
y = df['left']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create a Logistic Regression model with increased max_iter
model = LogisticRegression(random_state=42, max_iter=1000)

# Perform 5-fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
y_pred_cv = cross_val_predict(model, X_scaled, y, cv=cv, method='predict_proba')

# Convert probabilities to class predictions (0 or 1)
y_pred_class = (y_pred_cv[:, 1] > 0.5).astype(int)

# Plot the classification report
plt.figure(figsize=(8, 6))
sns.heatmap(pd.DataFrame(classification_report(y, y_pred_class, output_dict=True)).T, annot=True, cmap='viridis', fmt=".2f")
plt.title('Classification Report - Logistic Regression (5-Fold CV)')
plt.show()

# 5.2.	Train a Random Forest Classifier model and apply the 5-Fold CV and plot the classification report.
# Features and target variable
X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years']]
y = df['left']

from sklearn.ensemble import RandomForestClassifier
# Create a Random Forest Classifier model
model = RandomForestClassifier(random_state=42)

# Perform 5-fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
y_pred_cv = cross_val_predict(model, X, y, cv=cv, method='predict_proba')

# Convert probabilities to class predictions (0 or 1)
y_pred_class = (y_pred_cv[:, 1] > 0.5).astype(int)

# Plot the classification report
plt.figure(figsize=(8, 6))
sns.heatmap(pd.DataFrame(classification_report(y, y_pred_class, output_dict=True)).T, annot=True, cmap='viridis', fmt=".2f")
plt.title('Classification Report - Random Forest Classifier (5-Fold CV)')
plt.show()

# 5.3.	Train a  Gradient Boosting Classifier model and apply the 5-Fold CV and plot the classification report.

# Features and target variable
X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years']]
y = df['left']

from sklearn.ensemble import GradientBoostingClassifier

# Create a Gradient Boosting Classifier model
model = GradientBoostingClassifier(random_state=42)

# Perform 5-fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
y_pred_cv = cross_val_predict(model, X, y, cv=cv, method='predict_proba')

# Convert probabilities to class predictions (0 or 1)
y_pred_class = (y_pred_cv[:, 1] > 0.5).astype(int)

# Plot the classification report
plt.figure(figsize=(8, 6))
sns.heatmap(pd.DataFrame(classification_report(y, y_pred_class, output_dict=True)).T, annot=True, cmap='viridis', fmt=".2f")
plt.title('Classification Report - Gradient Boosting Classifier (5-Fold CV)')
plt.show()
