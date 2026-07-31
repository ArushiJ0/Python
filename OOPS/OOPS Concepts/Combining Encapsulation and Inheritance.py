
class Person:
    def __init__(self, name , age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name (self , new):
        self.__name = new
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self , new):
        self.__age = new

class Student(Person):
    def __init__(self , name, age , student_id):
        super().__init__(name, age)
        self.student_id = student_id

s = Student('Arushi', 18, 9736)
print(s.name,s.age,s.student_id)
s.name = 'Ruhi'
s.age = 90
print(s.name , s.age)
    
        
