

# This program showed that how to use __init__() method in class

class Homosapien:

    def __init__(self, name, age, no_of_hand, no_of_leg, specification):
        self.name = name
        self.age = age
        self.no_of_hand = no_of_hand
        self.no_of_leg = no_of_leg
        self.specification = specification

    def show_details(self):
        print("Name= ", self.name)
        print("Age= ", self.age)
        print("No of Hand= ", self.no_of_hand)
        print("No of Leg= ", self.no_of_leg)
        print("Specification= ", self.specification)


# object creation ...

man = Homosapien("Nabil", 19, 2, 2, "Human")
man.show_details()


print()


# Example of Inheritance:
#
"""
 
Rules of constructor:-
         
         class ClassName(ParentClass):
                variables
                names
                ----
                ----
 
"""

# Now I create an another class name Woman ... That inherit the Homosapien class

class Woman(Homosapien):
    pass


pinki = Woman("Pinki", 22, 2, 2, "Human")
pinki.show_details()

