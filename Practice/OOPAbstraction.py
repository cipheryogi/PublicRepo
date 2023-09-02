# Abstraction is a concept in object-oriented programming (OOP) that focuses on hiding unnecessary implementation details and exposing only the essential features of an object. It allows us to create simplified models of complex systems.

from abc import ABC, abstractmethod # two entities (ABC and abstractmethod) from the abc module

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Zzzz...")


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


# Creating instances of different classes
dog = Dog()
cat = Cat()

# Calling the abstract method
print(dog.sound())  # Output: "Woof!"
print(cat.sound())  # Output: "Meow!"

# Calling the non-abstract method
dog.sleep()  # Output: "Zzzz..."
cat.sleep()  # Output: "Zzzz..."

# In this example, we have an abstract base class Animal that defines an abstract method sound(). The Animal class is marked as abstract using the ABC module. Abstract methods are declared using the @abstractmethod decorator, and they must be overridden by the subclasses.The subclasses Dog and Cat inherit from the Animal class and provide their own implementations of the sound() method.
# By using abstraction, we can define a common interface (sound()) in the Animal class without specifying the exact implementation details for each subclass. This allows us to treat different animals uniformly without worrying about their specific behavior.
# n addition to the abstract method, the Animal class also has a non-abstract method sleep(), which is implemented directly in the base class. This method demonstrates that abstract classes can have concrete (non-abstract) methods as well.
# In the example, we create instances of Dog and Cat and call the sound() method on them, which outputs the respective sounds. We can also call the sleep() method on the objects, demonstrating that the non-abstract methods can be directly accessed from the abstract base class.
# Abstraction enables us to create a simplified and unified view of objects, focusing only on the essential characteristics and behaviors while hiding the implementation details.
# NOTE: The abc module in Python stands for "Abstract Base Classes" and provides mechanisms for defining abstract classes and abstract methods. Abstract base classes are classes that cannot be instantiated directly but are meant to serve as a blueprint for other classes.mporting ABC and abstractmethod from the abc module allows us to follow the principles of abstraction and create abstract classes that provide a common interface and enforce specific behaviors in their subclasses.
