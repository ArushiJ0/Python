class Vehicle:
    def start(self):
        print("starting message")

class Car(Vehicle):
    def start(self):
        print("Different msg")
        super().start()

c = Car()
c.start()
