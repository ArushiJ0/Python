class Animal :
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Dog")

class Cat(Animal):
    def speak(self):
        print("Cat")

animal = [Dog() , Cat()]
for i in animal:
    i.speak()
