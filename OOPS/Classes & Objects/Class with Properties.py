##Create a class named `Rectangle` with private attributes `length` and `width`. Use properties to get and set these attributes. Create an object of the class and test the properties.

class Rectangle:
    def __init__ (self,length,width):
        self.__l = length
        self.__w= width
        
    @property
    def length(self):
        return self.__l
    
    @length.setter
    def length(self,length):
        self.__l = length

    @property
    def width(self):
        return self.__w

    @width.setter
    def width(self,width):
        self.__w = width

r = Rectangle(40,30)
print(r.length, r.width)
r.length = 10
r.width = 12
print(r.length , r.width)
