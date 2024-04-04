# Assessment # 4: Handle the left Class Imbalance using SMOTE technique
# Here's the final result after performing all steps (4.3): 
# Accuracy: 0.99

# Confusion Matrix:
# [[2276   10]
#  [  15  699]]

# Classification Report:
#               precision    recall  f1-score   support

#            0       0.99      1.00      0.99      2286
#            1       0.99      0.98      0.98       714

#     accuracy                           0.99      3000
#    macro avg       0.99      0.99      0.99      3000
# weighted avg       0.99      0.99      0.99      3000


import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your dataset
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# # Step 1: Separate categorical and numerical variables
# categorical_cols = ['sales', 'salary']  # Add other categorical columns as needed
# numeric_cols = [col for col in df.columns if col not in ['left'] + categorical_cols]

# # Step 2: Apply get_dummies to categorical variables
# df_categorical = pd.get_dummies(df[categorical_cols], drop_first=True)

# # Step 3: Combine categorical and numeric variables
# df_processed = pd.concat([df[numeric_cols], df_categorical, df['left']], axis=1)

# # Separate features and target variable
# X = df_processed.drop('left', axis=1)
# y = df_processed['left']

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize the features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Apply SMOTE to handle class imbalance
# smote = SMOTE(random_state=42)
# X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# # Train a classifier (Random Forest, for example) on the resampled data
# clf = RandomForestClassifier(random_state=42)
# clf.fit(X_resampled, y_resampled)

# # Make predictions on the test set
# y_pred = clf.predict(X_test_scaled)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)

# print(f"Accuracy: {accuracy:.2f}")
# print("\nConfusion Matrix:")
# print(conf_matrix)
# print("\nClassification Report:")
# print(classification_rep)

# To perform a stratified split of the dataset into training and testing sets with a ratio of 80:20 and a random state of 123, we can use the train_test_split function from scikit-learn with the stratify parameter set to the target variable. 

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from imblearn.over_sampling import SMOTE
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# # Step 1: Separate categorical and numerical variables
# categorical_cols = ['sales', 'salary']  # Add other categorical columns as needed
# numeric_cols = [col for col in df.columns if col not in ['left'] + categorical_cols]

# # Step 2: Apply get_dummies to categorical variables
# df_categorical = pd.get_dummies(df[categorical_cols], drop_first=True)

# # Step 3: Combine categorical and numeric variables
# df_processed = pd.concat([df[numeric_cols], df_categorical, df['left']], axis=1)

# # Separate features and target variable
# X = df_processed.drop('left', axis=1)
# y = df_processed['left']

# # Step 4.1: Stratified split into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

# # Step 4.2: Standardize the features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Step 4.3: Apply SMOTE to handle class imbalance
# smote = SMOTE(random_state=42)
# X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# # Step 4.4: Train a classifier (Random Forest, for example) on the resampled data
# clf = RandomForestClassifier(random_state=42)
# clf.fit(X_resampled, y_resampled)

# # Step 4.5: Make predictions on the test set
# y_pred = clf.predict(X_test_scaled)

# # Step 4.6: Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)

# print(f"Accuracy: {accuracy:.2f}")
# print("\nConfusion Matrix:")
# print(conf_matrix)
# print("\nClassification Report:")
# print(classification_rep)

# To upsample the training dataset using the SMOTE technique, you can continue using the SMOTE class from the imbalanced-learn library. Here's the modified code:
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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

# Step 4.4: Train a classifier (Random Forest, for example) on the resampled data
clf = RandomForestClassifier(random_state=42)
clf.fit(X_resampled, y_resampled)

# Step 4.5: Make predictions on the test set
y_pred = clf.predict(X_test_scaled)

# Step 4.6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(classification_rep)

