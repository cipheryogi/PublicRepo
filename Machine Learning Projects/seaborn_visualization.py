import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
import pandas as pd
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]})

# Scatter plot using Seaborn
sns.scatterplot(x='x', y='y', data=data)

# Show the plot
plt.show()
