##Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary
Dict = {x:x**2 for x in range (1,6)}
new_dict = {key:value for value,key in Dict.items()}
print(new_dict)
