##Create a class named `Vector` with attributes `x` and `y`. Overload the `+` operator to add two `Vector` objects. Create objects of the class and test the operator overloading.

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, v2):
        return Vector(self.x+ v2.x, self.y+v2.y)
    
    def __str__(self):
        return f'Vector({self.x} , {self.y})'
        

v1 = Vector(4,6)
v2 = Vector(5,2)
print(v1+v2)
