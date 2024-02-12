# Import necessary libraries
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Let's create a simple dataset
# Hours studied and corresponding scores
data = {'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4],
        'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69]}
df = pd.DataFrame(data)

# Preparing the data
X = df.iloc[:, :-1].values  
y = df.iloc[:, 1].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the algorithm
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Making predictions
y_pred = regressor.predict(X_test)

# Comparing actual vs predicted
df = pd.DataFrame({'Hours': X_test.flatten(), 'Actual Score': y_test, 'Predicted Score': y_pred})
print(df)

# Evaluating the algorithm
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
