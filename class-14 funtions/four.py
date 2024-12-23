#How to invoke inner fuction from outside#Case No:1
def add():
    print("Addition")

x= add 
print(x) #<function add at 0x000001EFC954A340>
x() #Addition
x() #Addition
x() #Addition
