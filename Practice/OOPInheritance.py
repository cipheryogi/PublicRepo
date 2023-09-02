# In Python, inheritance is a powerful feature that allows a class to inherit properties and methods from another class. The class that inherits is called the "child" or "derived" class, and the class being inherited from is called the "parent" or "base" class. 
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("The dog barks.")


animal = Animal("Generic Animal")
animal.sound()  # Output: The animal makes a sound.

dog = Dog("Buddy")
dog.sound()     # Output: The dog barks.

# In the example above, we have two classes: Animal and Dog. The Dog class inherits from the Animal class using the syntax (Animal) in the class definition. This means that the Dog class inherits all the attributes and methods defined in the Animal class.

# When we create an instance of the Dog class (dog = Dog("Buddy")), we can access both the name attribute inherited from the Animal class and the sound() method overridden in the Dog class. This is because the Dog class inherits the __init__() constructor from the Animal class, allowing us to initialize the name attribute, and the sound() method is overridden in the Dog class to provide a specific implementation.

# Inheritance allows us to reuse code, promote code reusability, and create hierarchical relationships between classes. It also enables the child class to extend or modify the behavior defined in the parent class.

# Note that there are - multi-level inheritance, multiple inheritance (child derived from 2 or more parent classes), Hierarchical inheritance