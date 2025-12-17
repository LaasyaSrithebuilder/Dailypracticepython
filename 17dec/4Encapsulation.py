class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    @property
    def name(self): #getter
        return self.__name
    @name.setter
    def name(self, name):
        if name == "bob":
            "defaultname"
        else:
            self.__name = name

    @staticmethod # Static method doent require self parameter because it does not operate on object data it can be called directly from the class
    def nameis():
        print("This person is Alice.")


p = Person("Alice", 30)
print(p.name)  # Accessing the name using the getter

Person.nameis()  # Calling the static method
# p.name = "bob"  # Trying to set the name to "bob"
# print(p.name)  # Accessing the name again to see if it changed
    

