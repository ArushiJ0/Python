#Finding second largest number 
nums = [9 ,7 , 8, 4, 5, 6 ,1]
l = nums[0]
sl = 0 
for i in range (len(nums)):
    if nums[i]>l:
        l = nums[i]
    for i in range (len(nums)):
        if sl < nums[i] < l :
            sl = nums[i]
print(l)
print (sl)
        
