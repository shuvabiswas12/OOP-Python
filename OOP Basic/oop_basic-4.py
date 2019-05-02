
class Square:

    side = 3

    def __init__(self):
        self.side = 0

    def area(self):
        return self.side * self.side

ob = Square()
print(Square.side)
print(Square.area(ob))
print(ob.side)

ob.side = 4
print(ob.area())

del ob.side # this statement determined that if i create a variable outside the class then it cen be delete like this
print(ob.area())
