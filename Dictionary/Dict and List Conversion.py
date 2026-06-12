##Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
Dict = {x:x**2 for x in range (1,6)}
List = list(Dict.items())
print(List)
