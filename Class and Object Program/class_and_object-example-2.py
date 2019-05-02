
class Test:

    def __init__(self):
        self._x = None

    @property
    def x(self):
        print("Getter of x called")
        return self._x

    @x.setter
    def x(self, value):   # name must be same
        print("Setter of x called")
        self._x = value

    @x.deleter
    def x(self):   # name must be same
        print("Deleter of x called")
        del self._x


c = Test()
c.x = 'Test Program'  # setter called
foo = c.x  # getter called
del c.x  # deleter called

