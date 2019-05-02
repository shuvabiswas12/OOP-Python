
# inheritance in python ...

class Vehical:

    def __init__(self):
        print("Color = ",None)

    def speed(self):
        return self.x * self.x



car = Vehical()
car.x = 5
print(car.speed())


# example of inheritance
# inherit vehical class into car class ...
class Car(Vehical):
    def __init__(self):
        print("Color = ", None)

    def speed(self):
        return self.x * self.x

vehical = Car()
vehical.x = 10
print(vehical.speed())

print(Car.speed(car))
