class Shape:
    def __init__(self,color):
        self.color = color

class Circle(Shape):
    def __init__(self,radius,color):
        self.radius = radius
        super().__init__(color)

c = Circle('red', 8)
print(c.color,c.radius)
