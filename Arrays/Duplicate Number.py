#remove duplicate elements 
nums = [1,1,1,2,2,2,3,4,4,4,7,9,9,10]
n =[]
for i in range (len(nums)-1):
    if nums[i] != nums[i+1]:
        n.append(nums [i])
n.append(nums[-1])
print(n)
        
       

    

