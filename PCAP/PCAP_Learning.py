''' 

Math module / Math functions in scope - 
ceil(), floor(), trun() - their differences
hypot() - to calculate the hypotaneous of a right angle triangle.

Random modile / random library (import random)
random.see() , random.random() - basically by default Python keeps changing the sees based on the local timestamp to generate true random variables. However if we fix the seed to any integer then the random numbers generated remain constant for the seed.
random.choice() - returns a random value from a sequence/list/tuple
random.sample() - To be more precise, the function randomly selects the given number of unique elements (unique indexes) from the list but doesn't check whether the content of the elements are all different.
What does it mean in practice? Take a look:
random.sample(['Martin', 'John', 'Kate'], 2)
The line above will randomly select and return two of the three unique names from the list. You are guaranteed to get two names, and you are guaranteed that they will be two different names since there are no duplicated values in the list. However, take a look at this modified example: random.sample(['Martin', 'John', 'Martin'], 2)
Now, the list contains a duplicated value, but random.sample doesn't know that. It can randomly decide to return elements with indexes 0 and 1, and you will get ['Martin', 'John']. However, it can also randomly pick indexes 0 and 2, in which case you will get ['Martin', 'Martin'].
To sum up, random.sample picks elements with unique indexes but doesn't verify whether the elements at these indexes are unique.

Platform module

In the previous video, we've discussed platform.python_version_tuple(), which returns your Python version as a 3-element tuple, for example: ('3', '11', '4')
There's also another function that looks similar: platform.version(). This function, in turn, returns your system's release version as a single string, for example: 3.11.4
Keep in mind not to confuse these two functions for the PCAP exam!

import math, numpy, random, platform
for name in dir(platform):
    print(name,end='\t')
print(platform.platform())
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.python_implementation())
print(platform.python_version_tuple())
print(platform.python_version())

This content is outside the scope of the PCAP examination, but it may be very useful if you work with Python. I’ve mentioned that there are lots of modules written for Python by both professional Python developers and Python enthusiasts. But how can you find out what modules are available? Where can you find their code? One of the best sources of Python modules is the Python Package Index, or PyPI.
It is available at https://pypi.org/.
It is a repository full of Python modules, you can browse them and download them as you need. Have fun!


'''