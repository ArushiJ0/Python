import numpy as np

arr = np.random.randint(1,20, size =(5,5))
print(arr)
print("Mean :",np.mean(arr))
print("Standard deviation :",np.std(arr))
print("Variance :", np.var(arr))
print("Median :", np.median(arr))


arr2 = np.random.randint(1,10, size=(3,3))
mean = np.mean(arr2)
std = np.std(arr2)
normalize = (arr2 - mean)/std
print("Normalized Array : \n", normalize)

