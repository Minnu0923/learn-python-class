#version of eight.py
numbers=[10,78,14,96,117,11,31,42]


def check(num):
    return num%2 ==0
    
filter_obj= filter(check, numbers)
print(list(filter_obj))