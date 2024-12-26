#how to find file properties
'''file name, file is readable or not
file is writable or not
file is closed or not'''

fp=open('data.txt', 'r')
print(fp.name) #data.txt
print(fp.readable()) #true
print(fp.writable()) #false
print(fp.closed) #false
fp.close()
print("After closing")
print(fp.closed) #true

