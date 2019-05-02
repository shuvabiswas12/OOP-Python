
class Robot:

##    This is a constructor for python ...
    
##    def __init__(self, name, color, weight):
##        self.name = name
##        self.color = color
##        self.weight = weight



    def introduction(self):
        print("Hi, My name is "+self.name)



tom = Robot()
tom.name = 'TOM'
tom.color = 'red'
tom.weight = '30lbs'

##tom = Robot('Tom', 'red', '30lb')
tom.introduction()


zerry = Robot()
zerry.name = 'Zerry'
zerry.color = 'green'
zerry.weight = '50lbs'

##zerry = Robot('Zerry', 'green', '20lb')
zerry.introduction()



