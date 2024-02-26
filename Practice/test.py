import sys
import random
# Add the desired path to sys.path
# sys.path.append("/Users/yogesh.shinde/Library/Python/3.11/lib/python/site-packages")

import matplotlib.pyplot as plt

random_numbers = [random.randint(0, 99) for _ in range(100)]

plt.plot(random_numbers, marker='o')
plt.show()
