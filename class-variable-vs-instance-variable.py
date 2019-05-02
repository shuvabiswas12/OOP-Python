
class A:

    leg = 5  # class variable

    def __init__(self, value):
        self.money = value  # instance variable


a = A(10)
b = A(20)

print(a.money, ' ', b.money)
print(a.leg, ' ', b.leg)


A.leg = 100  # change the value of class variable
print(a.leg, ' ', b.leg)


a.leg = 200 # this a.leg variable is an object variable under a. This is not a class variable
print(a.leg, ' ', b.leg)

a.__class__.leg = 300  # another way of change the class variable
print(a.leg, ' ', b.leg)


