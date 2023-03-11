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

stu1 = Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
# user cannot accsees student class it will throww an error