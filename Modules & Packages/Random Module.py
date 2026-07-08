##Use the `random` module to generate a list of 5 random numbers between 1 and 50 and shuffle the elements of a list.

import random

num = [random.randint(1,50) for _ in range(5)]

print(num)

shuffle = list(range(1,21))
random.shuffle(shuffle)
print(shuffle)
