# In Python, a decorator is a design pattern that allows modifying the behavior of a function or a class without changing its source code directly. Decorators provide a way to add additional functionality to an existing function or class dynamically.
# In Python, a decorator is denoted by the @ symbol followed by the decorator function or class. It is placed above the definition of the function or class that is being decorated. When the decorated function or class is called or instantiated, the decorator is applied, altering or extending its behavior.

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())  # Output: "HELLO, WORLD!"

# another example - actually abstraction example which used the decorator. 
# Note: omitting the @abstractmethod decorator may not impact the output or functionality of the code. However, the use of the @abstractmethod decorator is crucial for achieving proper abstraction and adhering to the principles of object-oriented programming.The @abstractmethod decorator serves as a way to define abstract methods in abstract base classes. It helps enforce that any subclass of the abstract base class must provide an implementation for the abstract methods. This ensures that the subclasses conform to the contract defined by the base class, guaranteeing consistency in behavior across different implementations.
# IMPORTANT: Without the @abstractmethod decorator, the methods in the Shape class would be considered regular methods, and the derived classes would not be obligated to override them. This could lead to situations where a derived class unintentionally fails to provide an implementation for a required method, resulting in potential errors or unexpected behavior.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating an instance of Rectangle
rectangle = Rectangle(5, 3)

# Accessing abstract methods (abstraction in action)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())