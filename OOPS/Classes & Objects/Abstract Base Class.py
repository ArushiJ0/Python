##Create an abstract base class named `Shape` with an abstract method `area`. Create derived classes `Circle` and `Square` that implement the `area` method. Create objects of the derived classes and call the `area` method.

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r =r

    def area(self):
        return math.pi * self.r *self.r

class Square(Shape):
    def __init__(self, s):
        self.s =s

    def area(self):
        return self.s*self.s

c = Circle(5)
print(c.area())
S = Square(3)
print(S.area())
    
        
