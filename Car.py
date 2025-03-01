class Car :
    def __init__(self,MaxSpeed,Mileage):
        self.maxSpeed = MaxSpeed
        self.Mileage = Mileage
    def printObject(self):
        print("This car's Max Speed is",self.maxSpeed)
        print("This mileage is",self.Mileage,"per liter")

bmw = Car("126km/hr","10km")

bmw.printObject()