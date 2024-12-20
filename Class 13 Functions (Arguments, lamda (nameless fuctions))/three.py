#default argument: only one default value can be defined for postions
#the values will be considered only if default value is provided and missing specified argument
#defult argument should always be placed at the last
#def cal(a,b,c=100):
def cal(a=100,b=10,c=100):
    print(a+b+c)

cal(1,2,3) #6
#cal(1,2) #TypeError: cal() missing 1 required positional argument: 'c'
#cal(1,2) #103
cal(1) #SyntaxError: parameter without a default follows parameter with a default

    