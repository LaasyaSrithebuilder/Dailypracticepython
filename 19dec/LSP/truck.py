from vechile import Vechile

class Truck(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        if age> 20:
            return None #returning none instead of value which is not being consistet with baseclass 
        #returns runtime error
        return 2000 if age > 5 else 1000
    
    def refuel(self):
        print("Truck is refueling with diesel..")