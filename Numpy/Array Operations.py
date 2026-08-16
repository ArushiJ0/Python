import numpy as np

arr2 = np.random.randint(1,30, size=(3,4))
arr3 = np.random.randint(1,30, size=(3,4))
print("Array1",arr2)
print("Array2",arr3)

print("Addition",arr2 + arr3)
print("Substraction",arr2 - arr3)
print("Multiplication",arr2 * arr3)
print("Division",arr2 /arr3)



arr1 = np.random.randint(1,17,size=(4,4))
print(arr1)
print("Row Sum:" ,np.sum(arr1, axis =1))
print("Column Sum:" ,np.sum(arr1 , axis =0))


