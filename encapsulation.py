class Atm :
    # Constructor
    # special/magic/dunder methods
    def __init__(self):
        
        self.__pin = ""
        self.__balance = 0
        print(id(self))
        self.menu()
    """
    there is getter and setter to get and set the private class

    """
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
