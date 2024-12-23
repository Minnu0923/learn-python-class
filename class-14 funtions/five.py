#How to invoke inner fuction from outside#Case No:1
#this can be done using fuction aliasing method
def outer():
    print("inside outer fuction")
    def inner():
        print("inside inner fuction")

    return inner


inner= outer() #aliasing method
inner()
inner()

