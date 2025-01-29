#  Assessment # 3: Perform clustering of Employees who left based on their satisfaction and evaluation
# We will use the k-means algorithm to cluster employees based on their satisfaction level and last evaluation. The Elbow method is used to determine the optimal number of clusters. The final clusters are visualized, and a summary of each cluster is printed.
# Interpretation of the output graph: 
# As the number of clusters (k) increases, the inertia tends to decrease. This is because with more clusters, each cluster will have fewer points, and the centroids are closer to the individual points. However, there is a point where the rate of decrease in inertia slows down. This point is known as the "elbow." The "elbow" on the graph is the point where adding more clusters does not significantly reduce the inertia. The optimal number of clusters is often chosen at the point where the inertia starts to show diminishing returns or forms an "elbow." This is where the trade-off between reducing inertia and keeping the model simple is reasonable. Implication: In this case the inertia is decreasing smoothly without a clear elbow, so it's challenging to determine the optimal number of clusters. If there is a distinct elbow in the plot, it suggests that beyond that point, the reduction in inertia is marginal, and adding more clusters does not significantly improve the model.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load your dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
df = pd.read_excel('/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Course Progress/Machine Learning with Python/Project - Employee Turnover Analytics /1688640705_hr_comma_sep.xlsx')

# Select relevant columns for clustering
features = df[['satisfaction_level', 'last_evaluation']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow method
inertia = []
for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (within-cluster sum of squares)')
plt.title('Elbow Method for Optimal k')
plt.show()

# Choose the optimal number of clusters based on the Elbow plot
optimal_clusters = 3  # Adjust this based on the plot

# Perform k-means clustering
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(features_scaled)

# Visualize the clusters
plt.scatter(df['satisfaction_level'], df['last_evaluation'], c=df['cluster'], cmap='viridis')
plt.title('Employee Clusters based on Satisfaction and Evaluation')
plt.xlabel('Satisfaction Level')
plt.ylabel('Last Evaluation')
plt.show()

# Explore the characteristics of each cluster
cluster_summary = df.groupby('cluster').mean()
print(cluster_summary)

