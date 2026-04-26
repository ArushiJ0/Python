#List all the odd numbers 
max_num = int(input("Enter the max num:"))
nums =[]
for i in range(1,max_num):
    if i%2 != 0:
        nums.append(i)
print(nums)
    
