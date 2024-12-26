#read and write 
#read data.txt and create a new file wish.txt
fp1=open('data.txt', 'r')
data=fp1.read()
fp2=open('wish.txt','w' )

fp2.write(data)

print("file successfully created")

fp1.close()
fp2.close()