##Create a generator expression that generates the squares of numbers from 1 to 10. Iterate over the generator and print each value.

sq= (x**2 for x in range(0,11))

for i in sq:
    print(i)
