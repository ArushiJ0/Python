##Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list
import random
num = [random.randint(1,20)for _ in range(20)]
print(num)
print("Ascending order:", sorted(num))
print("Descending order:", sorted(num , reverse = True))
print("Unique elements:", list(set(num)))
