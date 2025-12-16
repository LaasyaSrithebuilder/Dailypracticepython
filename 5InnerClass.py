class Student:
    def __init__(self,name,rollno):# user passed arguments
        self.name = name
        self.rollno = rollno
        self.Desktop = self.Desktop() # creating object of inner class inside outer class constructor
    
    def show(self):
       # print(f"Name: {self.name}, Roll No: {self.rollno}")
        return self.name, self.rollno
        self.Desktop.show() # calling inner class method using outer class object
        
    #inner class inside Student class
    # we can create object of inner class using outer class object or we can create object 
    #of inner class directly inside outer class 

    class Desktop:

        def config(self,cpu,ram):
            self.cpu = cpu
            self.ram = ram
            print(f"CPU: {self.cpu}, RAM: {self.ram}")

        def show(self):
            print("This is show method of Desktop class")
            return self.cpu, self.ram



s1 = Student("Laasya",101)
s2 = Student("Sri",102)

des1 = s1.Desktop # creating object of inner class using outer class object


# Accessing instance variables show details

print(s1.show())
des1.config('i7',16) # Accessing inner class method using outer class object
res = s2.show()
print(res)


