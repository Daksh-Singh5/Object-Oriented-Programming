class Dog :
    def __init__(self,AvarageLifetime,Colour):
        self.AvarageLifetime = AvarageLifetime
        self.Colour = Colour
    def printObject(self):
        print("Your Dog Lives for about",self.AvarageLifetime)
        print("it is in",self.Colour,"colour")

goldenRetreaver = Dog("20 Years","Golden")
GremanSherperd = Dog("18 Years","Black")

GremanSherperd.printObject()
goldenRetreaver.printObject()


