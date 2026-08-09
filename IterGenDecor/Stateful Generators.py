def counter (start):
    count = start
    while True:
        yield count
        count +=1
        
counter = counter(0)
for _ in range (10):
    print(next(counter))
    
