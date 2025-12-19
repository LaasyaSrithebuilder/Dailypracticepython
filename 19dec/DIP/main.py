from vechile import Vechile
from insurancecal import InsuranceCalculator
from objectformatter import ObjectFormatter
from car import Car
from truck import Truck
from electriccar import ElectricCar
from maintanence import Maintanence
from brakeinspection import BrakeInspection

def main():
    car = Car("bmw","tata", 2018)
   # truck = Truck("tatasafari","ford",2015)
    truck = Truck("tatasafari","ford",1985)
    electriccar = ElectricCar("tesla","5.9",2024)
    car.refuel()
    truck.refuel()
    electriccar.recharge()
    
    insurancecal = InsuranceCalculator()
    formatter = ObjectFormatter()

    print(f" Car Incurance cost :${insurancecal.caluculate_vechile_insurance(car)+100}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(car)}")
    print(f"Incurance cost :${insurancecal.caluculate_vechile_insurance(truck)}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(truck)}")

    service= Maintanence(BrakeInspection())
    service.servicevechile(car)
if __name__ == "__main__":
    main()