# Assesssment # 6: Identify the best model and justify the evaluation metrics used.
# To compare the models and identify the best one, you can use the ROC/AUC (Receiver Operating Characteristic/Area Under the Curve) metric. This metric is commonly used for binary classification problems and provides an overall assessment of a model's performance across various classification thresholds. Here's how we can calculate ROC/AUC and plot the ROC curves for each model:

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_curve, auc
from imblearn.over_sampling import SMOTE

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

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

# Step 5: Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Upsample the training dataset using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# Step 7: Train models
lr_model = LogisticRegression(random_state=42)
rf_model = RandomForestClassifier(random_state=42)
gb_model = GradientBoostingClassifier(random_state=42)

models = [lr_model, rf_model, gb_model]
model_names = ['Logistic Regression', 'Random Forest', 'Gradient Boosting']

# Plot ROC curves
plt.figure(figsize=(10, 6))

for model, name in zip(models, model_names):
    model.fit(X_resampled, y_resampled)
    y_score = model.predict_proba(X_test_scaled)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')

# Plot the random classifier for reference
plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random Classifier')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Different Models')
plt.legend()
plt.show()

# To find the confusion matrix for each of the models, we can use the confusion_matrix function from scikit-learn. In this code: (1) The confusion_matrix function is used to calculate the confusion matrix for each model. (2) The sns.heatmap function from the seaborn library is used to visualize the confusion matrices. The confusion matrix provides a detailed view of the model's performance, showing the number of true positives, true negatives, false positives, and false negatives. It's a useful tool for understanding the strengths and weaknesses of a classification model. Adjust the code according to your specific requirements and dataset characteristics.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix  # Add this import statement
import seaborn as sns
from imblearn.over_sampling import SMOTE

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

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

# Step 5: Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Upsample the training dataset using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# Step 7: Train models
lr_model = LogisticRegression(random_state=42)
rf_model = RandomForestClassifier(random_state=42)
gb_model = GradientBoostingClassifier(random_state=42)

models = [lr_model, rf_model, gb_model]
model_names = ['Logistic Regression', 'Random Forest', 'Gradient Boosting']

# Calculate and plot confusion matrices
plt.figure(figsize=(15, 5))

for i, (model, name) in enumerate(zip(models, model_names), 1):
    plt.subplot(1, 3, i)
    
    model.fit(X_resampled, y_resampled)
    y_pred = model.predict(X_test_scaled)
    
    conf_mat = confusion_matrix(y_test, y_pred)
    sns.heatmap(conf_mat, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Left', 'Left'], yticklabels=['Not Left', 'Left'])
    
    plt.title(f'Confusion Matrix for {name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

plt.tight_layout()
plt.show()

# 6.3.From the confusion matrix, explain which metric needs to be used- Recall or Precision?
# The choice between recall and precision depends on the specific goals and requirements of the application, as well as the consequences of false positives and false negatives in the problem domain. 
# When to Use Recall: Use recall when the cost of false negatives (missing a positive instance) is high. For example, in a medical diagnosis scenario, if failing to identify a disease is more critical than falsely diagnosing a healthy person, prioritize recall.
# When to Use Precision:  Use precision when the cost of false positives (predicting positive incorrectly) is high. For instance, in a spam email detection system, if marking a legitimate email as spam has severe consequences, prioritize precision.
# F1 Score: If there is a balance between the importance of recall and precision, we might consider using the F1 score, which is the harmonic mean of recall and precision. F1 Score combines both recall and precision into a single metric and is useful when there is an uneven class distribution.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, confusion_matrix

# Assuming you have features X and target variable y
X = df.drop('left', axis=1)
y = df['left']

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X, columns=['sales', 'salary'], drop_first=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=123, stratify=y)

# Train a logistic regression model (you can use any model)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate confusion matrix
conf_mat = confusion_matrix(y_test, y_pred)

# Calculate precision and recall
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Print precision and recall values
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')

# Let's consider F1 score too assuming that we give balanced importance to false positives and false negatives.
# Calculate F1 Score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
print(f'F1 Score: {f1:.2f}')

# Conclusion:
# In the context of the employee turnover use case, where the goal is to predict whether an employee will leave the company, the choice between precision and recall depends on the specific priorities and consequences of false positives and false negatives. Let's consider the metrics:

# Precision (Positive Predictive Value): 0.63
# Precision measures the accuracy of the model when it predicts an employee will leave. A precision of 0.63 indicates that out of all employees predicted to leave, approximately 63% actually do leave. This is relevant if the cost of false positives (incorrectly predicting an employee will leave when they don't) is high.

# Recall (Sensitivity or True Positive Rate): 0.41
# Recall measures the ability of the model to capture all employees who actually leave. A recall of 0.41 indicates that approximately 41% of employees who actually leave are correctly identified by the model. This is relevant if the cost of false negatives (missing an employee who actually leaves) is high.

# F1 Score: 0.50
# F1 Score is the harmonic mean of precision and recall. It provides a balanced measure that considers both false positives and false negatives. A higher F1 Score indicates a better balance between precision and recall.

# Advice:

# If the cost of losing an employee is high:
# If the company incurs significant costs or challenges when an employee leaves, and minimizing false negatives (missing an employee who will leave) is a priority, we may want to prioritize recall. We want to identify as many employees at risk of leaving as possible.

# If the cost of false predictions is high:
# If there are substantial costs or negative consequences associated with incorrectly predicting that an employee will leave (false positives), we may want to prioritize precision. We want to ensure that when the model predicts an employee will leave, it is highly likely to happen.

# Consider the trade-off:
# Evaluate the business implications of false positives and false negatives. If both types of errors have significant consequences, We might consider a balance between precision and recall. 

#Ultimately, the decision should align with the business objectives and the specific consequences of making different types of errors in the context of employee turnover.
 
