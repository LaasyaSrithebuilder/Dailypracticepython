import json

class  Vechile:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year= year
    def caluculate_insurance_cost(self):
        age = 2024-self.year
        if age > 5:
            return 1000
        return 500 
    def to_json(self):
        return json.dumps({
            "VechileMake": self.make,
            "VechileModel": self.model,
            "VechileYear": self.year
        })
def main():
    vechile = Vechile("Toyota","carry",2018)
    print(f"Incurance cost :${vechile.caluculate_insurance_cost()}")
    print(f"Vehicle details in json :{vechile.to_json()}")
if __name__ == "__main__":
    main()

#in the above example the class vechile is performing multiple responsibilites which is violating srp 