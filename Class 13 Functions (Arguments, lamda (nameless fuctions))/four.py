#Variable length argument:
def cal (*nums):
    #print(nums)
    sum=0
    for num in nums:
        sum=sum+num
    
    print(sum)
    



cal(1)
cal(1,2)
cal(1,2,3)
cal(1,2,3,4)
cal(1,2,3,4,5)