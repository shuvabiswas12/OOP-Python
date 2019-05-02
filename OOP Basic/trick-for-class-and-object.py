
# here are some trick in python ...

class A:
    psss = 0

a = A()
print(a.__class__)

class B(A):
 def __init__(self):
     print("Inside the B")


b = B()
print(b.__class__)

# note:-
# ' object.__class__ ' return the class name

print(isinstance(b, B)) # isinstance() method return true or false
print(issubclass(B, A)) # issubclass() method return true or false
