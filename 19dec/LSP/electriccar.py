from vechile import Vechile

class ElectricCar(Vechile):
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        return 3000 if age > 5 else 1500
    
    def refuel(self):
        raise NotImplementedError("Electric cars will not be fuel")
    
    # breaks lsp since its not consistent with base class and should implement all the methods in parent i.e vechile 
    # but here refuel is not impllemented sice electric car as  no refuel option
    #  so we use next solid i -interface segreation to reduce this problem