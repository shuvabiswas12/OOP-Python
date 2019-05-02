

# class creation

class Restaurant:

    """

    1) by default in here a    __init__()   method that called constructor in other language.
    2) In python   __init__()   called a magic method since it has '_' .

    """

    def details(self):
        print("Name= ", self.name, 'Age= ', self.age)

    def details_with_address(self, address):
        print("Name= ", self.name, "Age= ", self.age)
        print("Address: ", address)


# object creation

restaurant = Restaurant()

restaurant.name = 'Object-1'
restaurant.age = 23

restaurant.details()

print()

restaurant.details_with_address(address='Ctg')





