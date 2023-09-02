# Encapsulation is one of the fundamental concepts of object-oriented programming (OOP) that helps organize and protect data and methods within a class. It involves bundling data (attributes) and the methods that operate on that data into a single unit called an object.
# A simple and concise example to explain encapsulation in Python can be a class representing a Person with private attributes and methods:
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def display_details(self):
        self.__print_name()
        self.__print_age()
        
    def __print_name(self):  # Private method
        print("Name:", self.__name)

    def __print_age(self):   # Private method
        print("Age:", self.__age)


# Creating an instance of the Person class
person = Person("John Doe", 25)

# Accessing public method to display details (encapsulation in action)
person.display_details()

# In this example, the Person class encapsulates the attributes __name and __age as private variables, denoted by the double underscores before their names. These attributes are not directly accessible from outside the class. Instead, the class provides a public method display_details() to display the encapsulated data.
# The private methods __print_name() and __print_age() are also encapsulated within the class and can only be called from within the class. They are used by the public method display_details() to print the encapsulated data.
# By encapsulating the attributes and methods, the class ensures that the internal implementation details are hidden and protected from external interference. The public method acts as an interface to access and manipulate the encapsulated data, promoting data integrity and security.
