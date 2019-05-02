
# How to create a class in python
# rules is given below ---

#
# class ClassName:
#     statement
#     ...
#     ...
#     ...


# example 1
# creating class in here ...
class Square:
    side = 0

    def area(self):
        return self.side * self.side


# creating a object of Square class
obj = Square()

obj.side = 5 # accessing the attribute of that class

value = obj.area() # accessing the method of that class

print(value)




# ---------------------------------------------------------------
# class 2
class Square2:

    def area(self):
        return self.side * self.side


obj2 = Square2()
obj2.side = 5   # we can create an attribute into a class like this... although there has not any attribute
result = obj2.area()
print(result)


# note :-  in python 'self' keyword must be given ... beacause of accessing the property of the class.
