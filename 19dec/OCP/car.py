from vechile import Vechile

class Car(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        #  added ocp
        return 1000 if age > 5 else 500