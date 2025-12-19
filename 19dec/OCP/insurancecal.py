from vechile import Vechile


class InsuranceCalculator:
    def caluculate_insurance_cost(self, vechile: Vechile):
        return vechile.calculate_insurance_cost()
    
# befoe ocp we need tio addd if another vechile object comes
# class InsuranceCalculator:
#     def caluculate_insurance_cost(self, vechile: Vechile):
#         age = 2024-vechile.year
#         if isinstance(vechile,Car): # violates ocp we are changing ther code for each and every new class adeed
#             return 1000 if age > 5 else 500
#         elif isinstance(vechile, Truck):
#             return 2000 if age>5 else 1000
        