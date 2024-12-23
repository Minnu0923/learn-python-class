#filter()
#is an inbuilt funtion- to filter values from a given sequence
#filter is executing provided fuction for elements of sequence


numbers=[10,78,14,96,117,11,31,42]


def check(num):
    if num %2 ==0:
        return True
    else:
        return False
    
filter_obj= filter(check, numbers)
print(list(filter_obj))

