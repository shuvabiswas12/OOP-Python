
class Car:

    _fuel = ''
    _color = ''
    _brand = ''

    """  This variable can be written in here 
    or can not be written in here. This is not matter.
    Because, the variables are defined in magic method using 'self' keyword. 
    If its defined in other method using 'self' keyword and it also be ok.  """

    def __init__(self, fuel, color, brand):
        self._fuel = fuel
        self._color = color
        self._brand = brand

    def details(self):
        pass

    def show_brand_name(self):
        pass

    def get_name(self):
        return self._brand


#
# another class that extends or inherit the Car class

class Motorcycle(Car):

        # method over riding

        def show_brand_name(self):
            print(self.get_name())


heroHonda = Motorcycle('2 liter', 'Blue', 'Hero Honda')
heroHonda.show_brand_name()
