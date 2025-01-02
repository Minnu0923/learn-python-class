class Test:
    def m1(self):
        print("Instance Method")
    @classmethod
    def m2(cls):
        print("Class Method")
    @staticmethod
    def m3():
        print("Static Method")

t1=Test()
t2=Test()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)