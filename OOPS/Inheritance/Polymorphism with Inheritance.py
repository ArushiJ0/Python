class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        print("Parrot")

class Penguin(Bird):
    def speak(self):
        print("Penguin")

b = [Parrot(), Penguin()]

for bird in b:
    bird.speak()
