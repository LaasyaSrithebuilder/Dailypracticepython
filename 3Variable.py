class Car():

    wheels = 5 # Class Variable sharesd by all objects shares class namespace

    def __init__(self):
        self.name = "ROOLLS ROYCE" # Instance Variable unique to each object shares object namespace
        self.color = 'White' # Instance Variable unique to each object shares object namespace
        #cnanges with each object

c1=Car()
c2=Car()

print(c1.name,c1.color,Car.wheels)
print(c2.name,c2.color,Car.wheels)

c2.color = 'Marron'

print(c2.name,c2.color,Car.wheels)