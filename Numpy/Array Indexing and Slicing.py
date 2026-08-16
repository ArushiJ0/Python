import numpy as np

arr1 = np.random.randint(1,37, size=(6,6))
print(arr1)
print("Sub Array:\n",arr1[2:5,1:4])

arr2 = np.random.randint(1,50, size =(5,5))
print(arr2)
print("Border Elements:\n" np.concatenate((arr2[0,:], arr2[-1,:],arr2[1:-1,0],arr2[1:-1,-1])))
