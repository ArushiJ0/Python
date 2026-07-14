##Create a class named `Address` with attributes `street`, `city`, and `zipcode`. Create a class named `Person` that has an `Address` object as an attribute. Create an object of the `Person` class and print its address.

class Address:
    def __init__ (self,street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self,address):
        self.address  = address

address = Address('xyz' , 'Indore',46005)
p = Person(address)
print(p.address.street, p.address.city, p.address.zipcode)
