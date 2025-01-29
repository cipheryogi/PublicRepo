import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

# Create barplot
sns.barplot(x=x, y=y)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Barplot Example')

# Show plot
plt.show()
