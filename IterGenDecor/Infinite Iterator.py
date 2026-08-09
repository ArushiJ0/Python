class InfiniteCounter:
    def __init__(self, n):
        self.n= n

    def __iter__(self):
        return self
    
    def __next__(self):
        self.n +=1
        return self.n
    
count = InfiniteCounter(0)
for _ in range(10):
    print(next(count))
        
