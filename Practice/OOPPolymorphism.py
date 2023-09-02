# Polymorphism is a key concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables different objects to respond to the same message or method invocation in different ways.
class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


# Polymorphic function
def make_sound(Polyobject):
    print(Polyobject.sound())


# Creating instances of different classes
dog = Dog()
cat = Cat()

# Polymorphic function call
make_sound(dog)  # Output: "Woof!"
make_sound(cat)  # Output: "Meow!"

# In this example, we have a common superclass Animal with a method sound(). The Animal class is inherited by two subclasses, Dog and Cat, which override the sound() method with their own implementations. 
# The make_sound() function demonstrates polymorphism by taking an object of the Animal class (or any of its subclasses) as a parameter. It then calls the sound() method on the object, regardless of its specific class.
# When we call make_sound(dog), the function invokes the sound() method on the dog object, resulting in the output "Woof!". Similarly, when we call make_sound(cat), it invokes the sound() method on the cat object, producing the output "Meow!".
# Polymorphism allows us to write generic code that can work with different objects, as long as they share a common interface (in this case, the sound() method from the Animal class). This flexibility and code reusability are some of the advantages of polymorphism in object-oriented programming.
#  Types - method overloading and operator overloading. 