class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r =r
    def area(self):
        return 3.14 * self.r**2

class Square(Shape):
    def __init__(self , side):
        self.side =side
    def area (self):
        return self.side**2

s = [Circle(2), Square(4)]
for shapes in s:
    print(shapes.area())
