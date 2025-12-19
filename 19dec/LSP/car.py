from vechile import Vechile

class Car(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        return 1000 if age > 5 else 500
    
    def refuel(self):
        print("Car is refueling with petrol..")