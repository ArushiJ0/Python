import numpy as np


arr1 = np.random.randint(1,21, size = (5,5))
print(arr1)

arr1[:,2] =1
print ("Array after manupilation:\n", arr1)

arr2 = np.random.randint(1,17,size =(4,4))
print(arr2)

np.fill_diagonal(arr2, 0)
print ("Array after manupilation:\n", arr2)
