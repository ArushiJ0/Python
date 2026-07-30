class Base1:
    def __init__(self,a):
        self.a=a

class Base2:
    def __init__(self,b):
        self.b=b

class Derived (Base1, Base2):
    def __init__ (self, a,b,c):
        self.c=c
        super().__init__(a)
        Base2.__init__(self,b)
        

obj = Derived('a','b','c')
print(obj.a, obj.b, obj.c)
