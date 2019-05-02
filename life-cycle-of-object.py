
class X:

    def __init__(self, name):
        self.name = name
        print(self.name + " created")

    def __del__(self):
        print(self.name + " deleted")


x = X('X')
y = X('Y')
print('Hello World')


def hello():
    m = X('Hello X')
    n = X('Hello Y')


hello()


