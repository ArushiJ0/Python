##Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

Set = {x for x in range(1,11)}
print(Set)
new_set = {x for x in Set if x%2 == 0}
print(new_set)
