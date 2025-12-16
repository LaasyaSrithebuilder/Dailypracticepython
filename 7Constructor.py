# class A:

#     def __init__(self):
#         print("Constructor of class A is called")   

#     def feauture1(self):
#         print("Feature 1 is working")

# class B(A): # Inheriting class A
#     def __init__(self):
#         super().__init__()  # Calling the constructor of class A if we want to call it.
#         #but if only it doesnt have init in its method .if it has it will call itself

#         print("Constructor of class B is called")

#     def feature3(self):
#         print("Feature 3 is working")



# a1 = A()
# b1 = B() # single level inheritance

# multilevel inheritance
class A:

    def __init__(self):
        print("Constructor of class A is called")   

    def feauture1(self):
        print("Feature 1a is working")

    def feature2(self):
        print("Feature 2 is working")

class B : 
    def __init__(self):
        print("Constructor of class B is called")

    def feature1(self):
        print("Feature 1b is working")

class C(A,B): # Inheriting class A
    def __init__(self):
        super().__init__()
          # it will call A since order is from left to right known as method resolution order(MRO)

        super().feature2() # it will call A's feature1 since A is first in MRO
        print("Constructor of class C is called")

    def feature4(self):
        print("Feature 4 is working")

c1 = C() # multilevel inheritance
c1.feauture1()
 
