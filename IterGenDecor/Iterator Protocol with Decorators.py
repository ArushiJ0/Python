def uppercase(cls):
    class Wrapper(cls):
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.text = self.text.upper()
    return Wrapper

@uppercase
class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -=1
            return self.text[self.index]


for i in ReverseString('Hello'):
    print(i)
    
