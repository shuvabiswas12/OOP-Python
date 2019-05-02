
# class and inheritance example 2

class Animal:

    # fields or property or variables

    # using '_' these are private variables and through this a variables can be private variable in python

    _name = ''
    _age = 0
    _color = ''
    _specification = ''

    def __init__(self, name='', age=0, color='', specification=''):
        self.set_name(name)
        self.set_age(age)
        self.set_color(color)
        self.set_specification(specification)

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_specification(self, spec):
        self._specification = spec

    def get_specification(self):
        return self._specification

    def details_view(self):
        print("Name= {name} \n"
              "Age= {age} \n"
              "Color= {color} \n"
              "Specification= {spec}".format(name=self.get_name(), age=self.get_age(), color=self.get_color(),
                                             spec=self.get_specification()))
        return


#
# another class

class Bird(Animal):
    pass


# creating object
beautifulBird = Bird('Koyel', 2, 'yellow', 'Birds')
beautifulBird.details_view()
