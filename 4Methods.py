class Student:
    school = "laasyas school"

    def __init__(self,sub1,sub2,sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
# Instance methods
    def avg(self):
        return (self.sub1 + self.sub2 + self.sub3)/3
    @classmethod #decorator to define class method
    def getSchoolNmae(cls):
        return cls.school
    @staticmethod #decorator to define static method
    def info():
        print("This is my school")

s1= Student(95,100,98)
s2= Student(96,100,90)
print("Average marks of student 1:",s1.avg())
print ("Average marks of student 2:",s2.avg())
Student.info()
print("School name is:",Student.getSchoolNmae())

