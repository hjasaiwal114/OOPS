
class Phone:
    """
    price, brand and camera are comman but os and ram are
    diffrent so we create supper to access parent class
    then access os and ram 
    """


    def __init__(self,price, brand, camera):
        print(" phele yha")
        self.__price = price
        self.brand = brand
        self.camera = camera
        print("Inside phone constructor")

class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os 
        self.ram = ram
        print("Inside smartphone constructor")
s = SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)

