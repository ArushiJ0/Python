##Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
Set = set(range(1,6))
List = list(Set)
List.append(6)
New_Set = set(List)
print(New_Set)
