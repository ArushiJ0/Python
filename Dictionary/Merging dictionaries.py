##Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
d1 = {x:x**2 for x in range (1,6)}
d2 = {y:y**2 for y in range(6,11)}
d3 = {**d1, **d2}
print(d3)
