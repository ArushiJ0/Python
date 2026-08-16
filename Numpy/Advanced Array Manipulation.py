import numpy as np
arr = np.random.randint(1,10,size=(3,3))
print("Array :\n", arr)
print("Reshaped Array:",arr.reshape(1,9))
print(" Again Reshaped Array:\n",arr.reshape(9,1))


arr1 = np.random.randint(1,10,size=(5,5))
print("Array\n:" , arr1)
Flattened_Array = arr1.flatten()
print("Flattened Array:" ,Flattened_Array)
print("Reshaped Array:\n" , Flattened_Array.reshape((5,5)))
