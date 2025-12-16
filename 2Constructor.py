class Computer:
    def __init__(self):
        self.age = 18
        self.name = "Laasya"

    def update(self,age):
        self.age = 22

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False


com1 = Computer()
com1.update(22)

com2 = Computer()

if com1.compare(com2):
    print("u are teens")
else:
    print("u are in 20s")
   
print(com1.name)
print(com2.name)