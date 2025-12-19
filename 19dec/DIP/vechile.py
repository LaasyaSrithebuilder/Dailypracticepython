from abc import ABC,abstractmethod

class  Vechile(ABC):#why abc bcoz no one should be able to change vechile mistakenly since it gets us runtime errors
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year= year

# indicates that each new object which instanstiates the vechile it should implement   insurance method
    @ abstractmethod 
    def caluculate_insurance_cost(self):
        pass 





