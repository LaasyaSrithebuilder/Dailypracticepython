class A:
    def feauture1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A): # Inheriting class A
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class D:
    def feature7(self):
        print("Feature 7 is working")   

class C(B,D): # Inheriting class B and d multiple inheritance
    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")

    
    
a1 = A()
print(a1.feauture1())
print(a1.feature2())

d1 = D()
print(d1.feature7())

b1 = B() # single level inheritance
print(b1.feature3())
print(b1.feature4())
print(b1.feauture1()) # accessing parent class method using child class object
print(b1.feature2()) 
 # accessing parent class method using child class object

c1 = C()# multilevel inheritance 
print(c1.feature5())            
print(c1.feature6())
print(c1.feature3()) # accessing grand parent class method using grand child class object   
print(c1.feauture1()) # accessing grand parent class method using grand child class object
print(c1.feature7()) # accessing parent class method using child class object