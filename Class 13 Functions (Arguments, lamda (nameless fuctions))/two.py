#keyword Argument: it defines the positional arguments with actual arguments, therefore the outcome will not change with change in position

def cal(a,b):
    print(a-b)

cal(a=100, b=50) #50

cal(b=50, a=100) #50

cal() #type error

