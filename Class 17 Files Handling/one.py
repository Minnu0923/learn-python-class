#file handling
fp=open('data.txt','r') #fp is file pointer: pointer is the begining of the file
data=fp.read()
print(data)
fp.close()

