""""example of udemey class"""
class User:
    
    def login(self):
        print("Login")
    def register(self):
        print("Regiter")

class Student(User):
    """
    by writing user i can accsess user class
    """

    def enroll(self):
        print("Enroll")
    
    def review(self):
        print("Review")