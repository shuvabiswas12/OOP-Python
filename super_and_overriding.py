
class A:
    var1 = 10
    var2 = 20

    def __init__(self):
        self.variable1 = 100
        self.variable2 = 200


class B(A):
    var2 = 10
    var1 = 20

    def __init__(self):
        # super().__init__()
        self.variable1 = 200
        self.variable2 = 100
        super().__init__()


b = B()
print(b.variable1)
print(b.var2)