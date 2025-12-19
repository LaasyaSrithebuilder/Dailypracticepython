from vechile import Vechile
from insurancecal import InsuranceCalculator
from objectformatter import ObjectFormatter
from car import Car
from truck import Truck
from electriccar import ElectricCar

def main():
    car = Car("bmw","tata", 2018)
   # truck = Truck("tatasafari","ford",2015)
    truck = Truck("tatasafari","ford",1985)
    #electriccar = ElectricCar("tesla","5.9",2024)
    vechiles = [car,truck]
    for vechile in vechiles:
        vechile.refuel()
    insurancecal = InsuranceCalculator()
    formatter = ObjectFormatter()
    print(f" Car Incurance cost :${insurancecal.caluculate_insurance_cost(car)}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(car)}")
    print(f"Incurance cost :${insurancecal.caluculate_insurance_cost(truck)}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(truck)}")
if __name__ == "__main__":
    main()