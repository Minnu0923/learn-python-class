class Account:
    def __init__(self):
        print("constuctor method")

    def m1(self):
        print("instance method")
    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
          print("static method - m3")


a1=Account()
a2=Account()
a3=Account()