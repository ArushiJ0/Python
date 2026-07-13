##Create a class named `Car` with attributes `make`, `model`, and `year`. Create an object of the class and print its attributes.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


##Add a method named `start_engine` to the `Car` class that prints a message when the engine starts. Create an object of the class and call the method.    
    def start_engine(self):
        print("When the engine starts")

        

car = Car('Audi', 'A21S', 2026)

print(car.make)
print(car.model)
print(car.year)
car.start_engine()
