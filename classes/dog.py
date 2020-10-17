class Dog:
    """ A simple attempt to model a dog. """

    def __init__(self, name, age):
        """ Initialize name and age attributes """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command """
        print(f"{self.name} rolled over!")


# Note about the __init__(self,.*) method:
# The __init__() method at ➌ is a special method that Python runs automatically 
# whenever we create a new instance based on the Dog class. This method has two 
# leading underscores and two trailing underscores, a convention that helps prevent 
# Python’s default method names from conflicting with your method names.
