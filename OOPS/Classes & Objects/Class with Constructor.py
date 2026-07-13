##Create a class named `Student` with attributes `name` and `age`. Use a constructor to initialize these attributes. Create an object of the class and print its attributes.

class Student:
    def __init__(self, name,age):
        self.name=name
        self.age=age

s1 = Student('John', 15)
print(s1.name, s1.age)
