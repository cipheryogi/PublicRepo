# keyword arguments example: position argument
def greetings(name, greeting):
    print(greeting, "!", name)
# call the function
greetings("Yogesh", "Hey");
#                                                   Intentional blank
# Keyword argument
greetings(greeting="Hi",name="Yogi")
#                                                   Intentional blank
# Defining functions with arbitary arguments
# Important: symbols used for passing argyments are (1) *args for non-keyword arguments and (2) **kwargs for keyword argyments
# this is useful when there's uncertainty on the number of arguments to pass for a given function
def total(*args):
    tot = 0
    for n in args:
        tot += n
    print(tot)
total(10);
total(10,10);
total(10,10,10,10,10);
# Notice that the function is now capable of accepting any number of arguments
# Now consider keyword variable number of arguments
def information(**kwargs):
    for key in kwargs.keys():
        print("Key: ",kwargs[key])
information(name = "Yogi", age = 43, city = "Pune", country = "India");
# Notice that the function is now capable of accepting any number of keyword arguments (basically key-value pairs). In keyword arguments its necessary to pass the value along with the key

        