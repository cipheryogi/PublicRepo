# In Python, access modifiers are a way to control the visibility and accessibility of variables and methods within a class. There are three commonly used access modifiers: public, protected, and private.
class MyClass:
    def __init__(self):
        self.public_var = 42

    def public_method(self):
        print("This is a public method.")

obj = MyClass()
print(obj.public_var)     # Output: 42
obj.public_method()       # Output: This is a public method.

# Protected Access Modifier: Protected variables and methods are intended to be accessed only within the class itself or its subclasses.To denote a protected member, we use a single underscore (_) prefix conventionally.
class MyClass:
    def __init__(self):
        self._protected_var = 42

    def _protected_method(self):
        print("This is a protected method.")

obj = MyClass()
print(obj._protected_var)       # Output: 42
obj._protected_method()         # Output: This is a protected method.

# Private Access Modifier: Private variables and methods are meant to be accessed only within the class that defines them. To denote a private member, we use a double underscore (__) prefix conventionally.
class MyClass:
    def __init__(self):
        self.__private_var = 42

    def __private_method(self):
        print("This is a private method.")

obj = MyClass()
# print(obj.__private_var)         # Error: AttributeError: 'MyClass' object has no attribute '__private_var'
# obj.__private_method()           # Error: AttributeError: 'MyClass' object has no attribute '__private_method'

# Remember that access modifiers in Python are more of a naming convention rather than strict enforcement. Developers are trusted to respect these conventions to maintain encapsulation and code integrity.