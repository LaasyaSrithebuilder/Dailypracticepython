from vechile import Vechile
from fuelable import Fuelable

class Car(Vechile, Fuelable):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        return 1000 if age > 5 else 500
    
    def refuel(self):
        print("Caars refueling with petrol")
    