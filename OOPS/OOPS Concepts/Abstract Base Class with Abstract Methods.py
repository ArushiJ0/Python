from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    def fuel_type(self):
        return "oil"

class Car(Vehicle):
    def start_engine(self):
        print("Car")
    def fuel_type(self):
        return "Petrol"

class Bike(Vehicle):
    def start_engine(self):
        print("Bike")
    def fuel_type(self):
        return"Bike_oil"

c = Car()
c.start_engine()
print(c.fuel_type())
b = Bike()
b.start_engine()
print(b.fuel_type())
