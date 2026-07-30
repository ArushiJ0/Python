##Create a base class named `Animal` with attributes `name` and `species`. Create a derived class named `Dog` that inherits from `Animal` and adds an attribute `breed`. Create an object of the `Dog` class and print its attributes.

##In the `Dog` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.

##In the `Dog` class, add a method named `bark` that prints a barking sound. Create an object of the class and call the method.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species = species

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name, species)
        self.breed =breed

    def bark(self):
        print("woof")
        
    def __str__(self):
        return f'({self.name},{self.species},{self.breed})'
        


d = Dog('Bruno','X','Pug')
print(d)
d.bark()
