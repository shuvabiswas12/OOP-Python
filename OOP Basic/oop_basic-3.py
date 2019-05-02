
# program 01
class Square:

    # this '__init__()' method work as like a constructor,
    # so, if i want to do some work during the object instantiation then '__init__()' must be declare

    def __init__(self):
        self.side = 4 # this variable is initialize during object creation

    def area(self) :
        return self.side * self.side

obj = Square()
area = obj.area()
print(area)



#----------------------------------------------------------------------




# program 02
class Square2:

    def __init__(self, x):
        self.side = x

    def area(self) :
        return self.side * self.side

obj = Square2(4) # i pass an attribute of a class and the value is initialize by '__init__()' method in class.
area = obj.area()
print(area)
