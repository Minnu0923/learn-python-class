def outer():
    print("inside outer funtion")

    def inner():
        print("insider outer fuction")
    
    inner()
    inner()




outer()