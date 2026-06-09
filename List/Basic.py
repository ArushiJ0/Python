##Create a list of the first 20 positive integers. Print the list
List = [num for num in range(1,21)]
print(List)
##Print the first, middle, and last elements of the list created in Assignment 1
print(List[0])
print(len(List) //2)
print(List[-1])
##Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
print("First five elements:" , List[:5])
print("Last five elements:", List[-5:])
print("Elements 5 to 15:", List[5:15])
