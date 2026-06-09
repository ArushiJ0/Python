##Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list
List = [num for num in range (1,11)]
List.remove(2)
List.remove(4)
List.remove(6)
List.insert(5,99)
print(List)
