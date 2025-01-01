fp=None
try:
    fp=open('emp.json','r')
    data=fp.read()

    a=int(input("Enter First Number"))
    b=int(input("Enter Second Number"))
    print(a+b)
except TypeError as te:
    print("type mismatch")
except FileNotFoundError as fnf:
    fp=open("default.json",'r')
except ValueError as ve:
    print("unable to convert")
finally:
    print("finally block will execute always")

    fp.close()