import numpy as np

Matrix1 = np.random.randint(1,20,size=(3,3))
print("Matrix 1:\n" ,Matrix1)
print("Inverse :\n", np.linalg.inv(Matrix1))
print("Determinant:\n",np.linalg.det(Matrix1))
print("EigenValues:\n",np.linalg.eigvals(Matrix1))


arr1 = np.random.randint(1,20, size=(2,3))
arr2 = np.random.randint(1,20,size=(3,2))

print("Array 1:\n",arr1)
print("Array 2:\n",arr2)
print("Multiplication:\n", np.dot(arr1, arr2))
