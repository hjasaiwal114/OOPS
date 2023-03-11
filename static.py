class Atm :
    # Constructor
    # special/magic/dunder methods
    def __init__(self):
        # instance variable
        
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1
        print(id(self))
        
        # self.__menu()
    """
    there is getter and setter to get and set the private class

    """
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.counter = new
        else:
            print("Not allowed")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("pin changed")

    def menu(self):
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit        
                        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            print("check balance")
        else:
            print("bye")
        
def create_pin(self):
    self.pin = input("Enter your pin")
    print("Pin set successfully")
def deposite(self):
    temp = input("Enter your pin")
    if temp == self.pin:
        amount = int(input("Enter the amount"))
        self.balance = self.balance + amount
    else:
        print("Invalid pin")
def withdraw(self):
    temp = input("Enter your pin")
    if temp == self.pin:
        amount = int(input("Enter the amount"))
        if amount < self.balance:
            self.balance = self.balance - amount
            print("Operation successful")
        else:
            print("insufficient funds")
    else:
        print("invalid function")
def check_balance(self):
    temp = input("Enter your pin")
    if temp == self.pin:
        print(self.balance)
    else:
        print("invalid pin")
