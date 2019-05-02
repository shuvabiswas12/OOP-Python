"""

__init__()

__add__()

__repr__()

__len__()

__str__()

"""


class TestDunderMethod:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return "TestDunderMethod('{}', '{}')".format(self.name, self.id)
        # return 'name: {} and id: {}'.format(self.name, self.id)

    def __str__(self):
        return '{} - {}'.format(self.name, self.id)

    def __add__(self, other):
        return self.id + other.id

    def __len__(self):
        return len(self.name)


test = TestDunderMethod("Shuva Biswas", 1000)

# print(test)  # automatically called dunder method (__repr__())
# print(test.__repr__())
# print(test.__str__())

print(repr(test))
print(str(test))  # automatically called dunder method (__str__())

test1 = TestDunderMethod("Biswas", 1400)
print(test + test1)  # automatically called dunder method (__add__())

print(len(test))  # automatically called dunder method (__len__())

# print(test.__len__())
# print(int.__add__(22, 20))
