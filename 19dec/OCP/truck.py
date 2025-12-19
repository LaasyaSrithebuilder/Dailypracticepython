from vechile import Vechile

class Truck(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        #  added ocp
        return 2000 if age > 5 else 1000