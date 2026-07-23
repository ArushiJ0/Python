##Create a class named `Counter` with a class variable `count`. Each time an object is created, increment the count. Add a method to get the current count. Create multiple objects and print the count.

class Counter:
    count = 0
    
    def __init__(self):
        Counter.count +=1
        
    @classmethod
    def current(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.current())
