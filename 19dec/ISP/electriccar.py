from vechile import Vechile
from rechargable import Rechargable
class ElectricCar(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        return 3000 if age > 5 else 1500
    
 
    def recharge(self):
        print("Electric car is being recharged")