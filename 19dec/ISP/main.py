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
    electriccar = ElectricCar("tesla","5.9",2024)
    car.refuel()
    truck.refuel()
    electriccar.recharge()
    #eeverything works correct but we missed lsp every method of parent class should be implemented
    #here in car and truck recharge is not implemented and electrice car refuel is not so follow isp
    # instead of one large concrete class methods like refuel recharge
    #just use small interfaces or abstract methods seperately and access only what is needed
    insurancecal = InsuranceCalculator()
    formatter = ObjectFormatter()

    print(f" Car Incurance cost :${insurancecal.caluculate_vechile_insurance(car)}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(car)}")
    print(f"Incurance cost :${insurancecal.caluculate_vechile_insurance(truck)}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(truck)}")
if __name__ == "__main__":
    main()