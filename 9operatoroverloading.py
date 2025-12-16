class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2   
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {} ". format(self.m1 ,self.m2 )# returns as string


s1 = Student(58,69)
s2 = Student(78,89)# Adding two objects
s3 = s1 + s2 # This will give error without __add__ method
# we are saying for Student.__add__(self,other) method when we use + operator between two objects of Student class
print(s3.m1, s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1) # This will print the object location without __str__ method so lets override it  
print(s1.__str__()) # This will print the as tuple returned from __str__ method 