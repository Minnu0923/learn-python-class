#Positional Argument: if you change the position of the arguments the outcome changes

def cal(a,b):
    print(a-b)

cal(100,50) #50
cal(50,100) #-50
cal () #TypeError: cal() missing 2 required positional arguments: 'a' and 'b'

