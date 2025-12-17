from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def printdata():
        """to implement in derived class"""
        pass

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def getInstance(name, age):
        if PersonSingleton.__instance is None:
            PersonSingleton("deafultname", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self


    def printdata(self):
        print(f"Name: {self.name}, Age: {self.age}")
p = PersonSingleton.getInstance("Alice", 30)
print(p)
a=p.printdata()
print(a)
q = PersonSingleton.getInstance("Bob", 25)
print(q)
q.printdata()#doesnot allow to create new instance, returns the first instance