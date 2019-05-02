
class MySoft:

    # class variable

    num_of_obj = 0
    raise_amount = 1.04

    def __init__(self, first, last, email, pay):

        # instance variable

        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

        MySoft.num_of_obj = MySoft.num_of_obj + 1

    def full_name(self):
        return self.first + ''.join(self.last)

    def apply_raise(self):
        return self.pay * self.raise_amount


myObj2 = MySoft("Test", "User", "testuser@gmail.com", '10')
myObj1 = MySoft("Shuva", 'Biswas', 'shuvabiswas@email.com', "20")

print(MySoft.num_of_obj)

print(myObj1.__dict__)
print(myObj2.__dict__)
print(MySoft.__dict__)
