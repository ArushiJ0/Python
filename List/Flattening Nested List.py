def flat_list(List):
     List = [x for y in nested_list for x in y]
     return List

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

print("Nested List:", nested_list)

flattened = flat_list(nested_list)
print("Flattened List:", flattened)
