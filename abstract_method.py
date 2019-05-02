from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printAreas(self):
        pass

class Ractangle(Shape):

    def printAreas(self):
        print("This is an override method")

    def displayName(self):
        print(__name__)

rac = Ractangle()
rac.displayName()


