# class Customer:

#     def __init__(self,name):
#         self.name = name

# def greet(customer):
#     print(id(customer))
#     customer.name = " Nitish"
#     print(customer.name)
#     print(id(customer))

# cust = Customer("Ankita")
# print(id(cust))

# greet(cust)

# print(cust.name)

"""When a variable is passed by reference, the function or method receives a reference to the memory location where the variable is stored, rather than a copy of the variable's value. This means that any changes made to the variable within the function or method will be reflected in the original variable outside of the function or method.

Passing by reference is often used when a function or method needs to modify a variable or object in place, rather than returning a new value. It can also be used to improve the efficiency of the program, as passing by reference avoids making unnecessary copies of large data structures."""
class Customer:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def intro(self):
        print("I am ", self.name, "and i am ", self.age)

c1 = Customer("Nitish", 34)
c2 = Customer("Ankit", 45)
c3 = Customer("Neha",32)

L = [c1 , c2, c3]

for i in L:
    i.intro()
