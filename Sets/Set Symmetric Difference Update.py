##Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}
s1.symmetric_difference_update(s2)
print(s1)
