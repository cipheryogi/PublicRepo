class demo():
    pass

obj = demo()
print(obj) # Output: <__main__.demo object at 0x1048d2ad0>


# example of data attributes - these can be shared only within the specified instance

class Health:
    #init function as constructor
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc
    #another method to display data
    def print_info(self):
        print("Health info: ")
        print("name: ", self.name)
        print("age: ", self.age)
        print("loc :", self.loc)

h1 = Health("Yogesh", 54, "Pune");
h1.print_info();

# example of class attributes - these are shared by all the instances

class Circle:
    # Class attribute
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius**2

# Create instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)

# Access the class attribute
print(circle1.pi)  # Output: 3.14159
print(circle2.pi)  # Output: 3.14159

# Access the instance attribute
print(circle1.radius)  # Output: 5
print(circle2.radius)  # Output: 3

# Call the instance method
print(circle1.calculate_area())  # Output: 78.53975
print(circle2.calculate_area())  # Output: 28.27431

# In this example, the Circle class has a class attribute pi, which represents the mathematical constant pi. Class attributes are defined directly within the class but outside of any methods. They are shared among all instances of the class.

# The __init__ method is the constructor that initializes the radius instance attribute. Each instance of the Circle class can have a different radius value.

# The calculate_area method is an instance method that calculates the area of the circle using the formula pi * radius^2. It accesses the pi and radius attributes of the instance using the self keyword.

# By accessing the class attribute pi through instances circle1 and circle2, we can see that it is the same value for all instances. Similarly, we can access the instance attribute radius specific to each instance.

# Finally, the calculate_area method is called on each instance, and it returns the calculated area of the circle based on the instance's radius attribute and the class attribute pi.
