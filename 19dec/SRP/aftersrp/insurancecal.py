from vechile import Vechile

class InsuranceCalculator:
    def caluculate_insurance_cost(self, vechile: Vechile):
        age = 2024-self.year
        if age > 5:
            return 1000
        return 500 
    