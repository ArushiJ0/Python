##Create a tuple with the first 10 positive integers. Print the tuple
Tuple = tuple(range(1,11))
print(Tuple)
##Print the first, middle, and last elements of the tuple created in Assignment 1.
print(Tuple[0])
print(f"{Tuple [len(Tuple)//2]}")
print(Tuple[-1])

##Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.

print(Tuple[:3])
print(Tuple[-3:])
print(Tuple[2:5])
