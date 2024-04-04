# Assessment # 5: Perform 5-Fold cross-validation model training and evaluate performance.
# To train a Logistic Regression model using 5-fold cross-validation and plot the classification report, we can use the cross_val_predict function from scikit-learn for predictions and then use the classification_report from scikit-learn to generate the report. Here we will use 'cross_val_predict' to perform 5-fold cross-validation with a Logistic Regression model and obtain predicted values. The classification report is then generated and plotted using a bar chart for each class (0: not left, 1: left).

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_predict
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Step 1: Separate categorical and numerical variables
categorical_cols = ['sales', 'salary']  # Add other categorical columns as needed
numeric_cols = [col for col in df.columns if col not in ['left'] + categorical_cols]

# Step 2: Apply get_dummies to categorical variables
df_categorical = pd.get_dummies(df[categorical_cols], drop_first=True)

# Step 3: Combine categorical and numeric variables
df_processed = pd.concat([df[numeric_cols], df_categorical, df['left']], axis=1)

# Separate features and target variable
X = df_processed.drop('left', axis=1)
y = df_processed['left']

# Step 4.1: Stratified split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

# Step 4.2: Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4.3: Upsample the training dataset using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# Step 5: Train a Logistic Regression model using 5-fold cross-validation
lr_model = LogisticRegression(random_state=42)
y_pred_cv = cross_val_predict(lr_model, X_resampled, y_resampled, cv=5)

# Plot the classification report
class_rep = classification_report(y_resampled, y_pred_cv, output_dict=True)
class_rep_df = pd.DataFrame(class_rep).transpose()

# Plot the classification report
fig, ax = plt.subplots(figsize=(8, 5))
class_rep_df[:-1].plot(kind='bar', ax=ax)
plt.title('Classification Report for Logistic Regression (5-Fold CV)')
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.show()

# Plot the confusion matrix using seaborn
conf_mat = confusion_matrix(y_resampled, y_pred_cv)
plt.figure(figsize=(8, 8))
sns.heatmap(conf_mat, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Left', 'Left'], yticklabels=['Not Left', 'Left'])
plt.title('Confusion Matrix for Logistic Regression')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# train a Random Forest Classifier model using 5-fold cross-validation and plot the classification report. This code uses a Random Forest Classifier, performs 5-fold cross-validation, and plots the resulting classification report and confusion matrix using seaborn.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Step 1: Separate categorical and numerical variables
categorical_cols = ['sales', 'salary']  # Add other categorical columns as needed
numeric_cols = [col for col in df.columns if col not in ['left'] + categorical_cols]

# Step 2: Apply get_dummies to categorical variables
df_categorical = pd.get_dummies(df[categorical_cols], drop_first=True)

# Step 3: Combine categorical and numeric variables
df_processed = pd.concat([df[numeric_cols], df_categorical, df['left']], axis=1)

# Separate features and target variable
X = df_processed.drop('left', axis=1)
y = df_processed['left']

# Step 4: Train a Random Forest Classifier model using 5-fold cross-validation
rf_model = RandomForestClassifier(random_state=42)
y_pred_cv_rf = cross_val_predict(rf_model, X, y, cv=5)

# Plot the classification report
class_rep_rf = classification_report(y, y_pred_cv_rf, output_dict=True)
class_rep_df_rf = pd.DataFrame(class_rep_rf).transpose()

# Plot the classification report
fig, ax = plt.subplots(figsize=(8, 5))
class_rep_df_rf[:-1].plot(kind='bar', ax=ax)
plt.title('Classification Report for Random Forest Classifier (5-Fold CV)')
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.show()

# Plot the confusion matrix using seaborn
conf_mat_rf = confusion_matrix(y, y_pred_cv_rf)
plt.figure(figsize=(8, 8))
sns.heatmap(conf_mat_rf, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Left', 'Left'], yticklabels=['Not Left', 'Left'])
plt.title('Confusion Matrix for Random Forest Classifier')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# train a Gradient Boosting Classifier model using 5-fold cross-validation and plot the classification report. This code uses a Gradient Boosting Classifier, performs 5-fold cross-validation, and plots the resulting classification report and confusion matrix using seaborn. 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Step 1: Separate categorical and numerical variables
categorical_cols = ['sales', 'salary']  # Add other categorical columns as needed
numeric_cols = [col for col in df.columns if col not in ['left'] + categorical_cols]

# Step 2: Apply get_dummies to categorical variables
df_categorical = pd.get_dummies(df[categorical_cols], drop_first=True)

# Step 3: Combine categorical and numeric variables
df_processed = pd.concat([df[numeric_cols], df_categorical, df['left']], axis=1)

# Separate features and target variable
X = df_processed.drop('left', axis=1)
y = df_processed['left']

# Step 4: Train a Gradient Boosting Classifier model using 5-fold cross-validation
gb_model = GradientBoostingClassifier(random_state=42)
y_pred_cv_gb = cross_val_predict(gb_model, X, y, cv=5)

# Plot the classification report
class_rep_gb = classification_report(y, y_pred_cv_gb, output_dict=True)
class_rep_df_gb = pd.DataFrame(class_rep_gb).transpose()

# Plot the classification report
fig, ax = plt.subplots(figsize=(8, 5))
class_rep_df_gb[:-1].plot(kind='bar', ax=ax)
plt.title('Classification Report for Gradient Boosting Classifier (5-Fold CV)')
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.show()

# Plot the confusion matrix using seaborn
conf_mat_gb = confusion_matrix(y, y_pred_cv_gb)
plt.figure(figsize=(8, 8))
sns.heatmap(conf_mat_gb, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Left', 'Left'], yticklabels=['Not Left', 'Left'])
plt.title('Confusion Matrix for Gradient Boosting Classifier')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
