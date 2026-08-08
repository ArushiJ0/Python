class Countdown:
    def __init__(self, n):
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<=0:
            raise StopIteration
        else:
            self.n -=1
            return self.n


for i in Countdown(5):
    print(i)
            
