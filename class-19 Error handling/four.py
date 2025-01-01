try:
    
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    #print(a+b+R) #type error
    print("a Value:", a, "b Value:",b)
    fp=open('emp.json','r')
    data=fp.read()
    print(data)
 
except TypeError as te:
    print("Type Mismatch")
    
except ValueError as ve:
    print("Unable to Convert")

except:
    print("please check the code")   
    #syntax error if kept on top( default 'except':must be last"
    #"catch-all" always keep it at last to catch errors accurately

finally:
    print("finally Block will execute always")
fp.close()

