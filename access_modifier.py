
class Employee:
    var = 9  # public variable
    _protected = "This is a protected variable"  # protected variable
    __private = "This is a private varible"  # private variable



emp = Employee()
print(emp.var)
print(emp._protected)
# print(emp.__private)  # this line creates an error
print(emp._Employee__private)  # this is correct form

# "emp._Employee.__private" means it is an min angle way to access the private variable



