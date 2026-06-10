##Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
def Tuple(T):
    Min = min(T)
    Max = max(T)
    Sum = sum(T)
    return Min, Max, Sum

T = (1,2,3,4,5)
Val = Tuple(T)
print(Val)
