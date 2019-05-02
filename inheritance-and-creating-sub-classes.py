
class A:

    def __init__(self, pay, amount):
        self.pay = pay
        self.amount = amount

    def view_all(self):
        return 'pay = ', self.pay + 'amount = ', self.amount


class B(A):

    def __init__(self, pay, amount, data):

        # one way to call parent class constructor

        A.__init__(self, pay, amount)  # this way it takes a 'object' parameter at first

        # another way to call parent class constructor

        super().__init__(pay, amount)

        self.data = data


b = B(1.04, 20000, True)
print(help(B))


#
# isinstance() method ...

if isinstance(b, B):
    print("b is an instance of B()")
else:
    print("b is not an instance of B()")


#
# issubclass() method ...

if issubclass(B, A):
    print("B is a sub class of A")
else:
    print("B is not a subclass of A")
