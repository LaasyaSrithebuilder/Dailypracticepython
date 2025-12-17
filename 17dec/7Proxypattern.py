from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def personmethod():
        "" " Interface method"""
class Person(IPerson):
    def personmethod(self):
        print("This is normal person.")

class PersonProxy(IPerson):
    def __init__(self):
        self._person = Person()

    def personmethod(self):
        print("Proxy person calling .")
    
p1 = Person()
p1.personmethod()

p2 = PersonProxy()
p2.personmethod()
