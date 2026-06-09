##Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
Tuple = tuple(range(1,6))
List = list(Tuple)
List.append(6)
New_Tuple = tuple(List)
print(New_Tuple)
