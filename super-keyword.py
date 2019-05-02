class Math:

    def __init__(self, x=2, y=2):
        self.x = 0
        self.y = 0

    def sum(self):
        return self.x + self.y


class ExtendMath(Math):

    def __init__(self, x=4, y=7):
        super().__init__(x, y)
        # self.x = 2
        # self.y = 5
        pass

    def subtract(self):
        return self.x - self.y


math = ExtendMath()

# if in the class, there are no field, than it have to be created object variable like math.x and math.y

#math.x = 4
#math.y = 6

print(math.subtract())
print(math.sum())
