##Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
Dict ={ x:x**2 for x in range(1,11)}
print(Dict)

##Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print("Value of key 5:", Dict[5])
print(Dict.keys())

##Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
Dict[11]=121
print(Dict)
del Dict[1]

print(Dict)

##Iterate over the dictionary created in Assignment 1 and print each key-value pair.

for key,value in Dict.items():
    print(f"{key}:{value}")
