
import datetime


class MyEmployee:

    num_of_object = 0  # class variable
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, email, pay):
        self.first = first  # instance variable
        self.last = last  # instance variable
        self.email = email  # instance variable
        self.pay = pay  # instance variable

    def full_name(self):
        return self.first+' '+self.last

    @classmethod  # this annotation is used for declare a class method
    def from_string(cls, emp_string):  # this 'cls' attributes takes that class automatically
        first, last, email = emp_string.split('-')
        return cls(first, last, email, 5000)  # this line returns an object of Employee class

    @classmethod
    def set_raise_amount(cls, amount):  # the 'cls' attributes the MyEmployee class automatically
        cls.raise_amount = amount

    @staticmethod  # this annotation is used for declare a static method
    def is_workday(day):  # this static method do not takes class or object as a parameter anymore
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = MyEmployee.from_string("Shuva-Biswas-shuvabiswas@email.com")

print(emp_1.full_name())

my_date = datetime.date(2017, 11, 13)
print(my_date)
print(MyEmployee.is_workday(my_date))


'''

Note:-
---------

Similarity: Both of them can be called on the Class itself, rather than just the instance of the class.
So, both of them in a sense are Class's methods. 

Difference: A class method will receive the class itself as the first argument, while a staticmethod does not


'''