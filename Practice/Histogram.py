import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9, 10]

# Create a histogram
plt.hist(data, bins=5, edgecolor='k', alpha=0.7)

# Customize the plot
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the histogram
plt.show()

# data is the list of values for which you want to create a histogram.
# plt.hist(data, bins=5) creates a histogram with 5 bins. You can adjust the number of bins to change the granularity of the histogram.
# edgecolor specifies the color of the edges of the bars.
# alpha controls the transparency of the bars.