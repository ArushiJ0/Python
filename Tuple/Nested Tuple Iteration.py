##Create a nested tuple and iterate over the elements, printing each element.
Tuple = ((1,2,3),(4,5,6),(7,8,9))
for i in Tuple:
    for j in i:
        print(j)
