from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def personmethod():
        "" " Interface method"""
class Student(IPerson):
    def __init__  (self):
        self.name = "JOHN"
    @staticmethod
    def personmethod():
        print("This is a student .")
class Teacher(IPerson):
    def __init__  (self):
        self.name = "MARRY"
    @staticmethod
    def personmethod():
        print("This is a teacher .")
class PersonFactory:
    @staticmethod
    def getperson(person_type: str) :
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        else:
            raise ValueError("Unknown person type")

if __name__ == "__main__":
    choice = input("Enter person type?\n")
    person = PersonFactory.getperson(choice)
    person.personmethod()