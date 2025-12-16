class Computer:
    def __init__(self,cpu,ram):
         self.cpu = cpu
         self.ram = ram
         print("Computer Configured")
    def config(self):
        print("Computer Configuration: ", self , self.cpu , "," , self.ram)

com1 = Computer('i5', '8gb') 
com2=Computer('i7', '16gb')


com1.config()
com2.config()

