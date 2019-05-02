
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} class, Obj name: {self.name}'


person = Person("Arijona")
print(person.__str__())
