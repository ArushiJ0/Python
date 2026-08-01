class Flyer:
    def fly(self):
        print("fly")
class Swimmer:
    def swim(self):
        print("swim")

class Superhero(Flyer, Swimmer):
    def fly(self):
        print("Superhero flies")
    def swim(self):
        print("Superhero swims")


s = Superhero()
s.fly()
s.swim()
