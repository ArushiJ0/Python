class Animal:
    pass
class Cat(Animal):
    pass

a = Animal()
c = Cat()

print(isinstance(a, Animal))
print(isinstance(c, Cat))
