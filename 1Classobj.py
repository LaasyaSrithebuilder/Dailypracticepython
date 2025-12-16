class Computer:

    def config(self):
        print("I5 processor, 16GB RAM, 1TB SSD")

com1 = Computer() # Constructor inbuilt
com2=Computer() # com1 , com2 are objects belong to thje class computer

# Calling method through class object

com1.config()
com2.config()

# calling method through class name

Computer.config(com1) # PASSING OBJECT AS PARAMETER
Computer.config(com2)
