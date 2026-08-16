import numpy as np

arr = np.random.randint(1,10, size = (3,3))
print ("Array 1:\n " ,arr)
arr2 =  np.random.randint(1,20, size = (3,))
print("Row Array:" ,arr2)

print("After Broadcasting :\n" ,arr+arr2)

arr3= np.random.randint(1,20, size=(4,4))
print("Array 2 :\n" , arr3)
arr4 = np.random.randint(1,20,size=(4,))
print("Column Array:" , arr4)

print("After Broadcasting\n :" ,arr3 - arr4[:,np.newaxis])
