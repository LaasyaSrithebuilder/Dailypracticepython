from vechile import Vechile
from insurancecal import InsuranceCalculator
from objectformatter import ObjectFormatter

def main():
    vechile = Vechile("Toyota","carry",2018)
    insurancecal = InsuranceCalculator()
    formatter = ObjectFormatter()
    print(f"Incurance cost :${insurancecal.caluculate_insurance_cost}")
    print(f"Vehicle details in json :{formatter.vechile_to_json(vechile)}")
if __name__ == "__main__":
    main()