class Flyer:
    def fly(self):
        print("Flying msg")

class Swimmer:
    def swim(self):
        print("Swimming msg")

class Superhero(Flyer, Swimmer):
    pass

s = Superhero()
s.fly()
s.swim()
