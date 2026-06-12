##Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

Dict = {x:x**2 for x in range(1,11)}
new_dict = {key:value for key,value in Dict.items() if key%2 ==0 }
print(new_dict)
