#Find the largest element
nums = [55, 32, 97,99,3,67]
largest = nums[0]
length = len(nums)
for i in range(length):
    if nums[i] > largest:
        largest = nums[i]
print(largest)
