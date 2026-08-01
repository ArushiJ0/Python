from abc import ABC , abstractmethod

class Appliance(ABC):
    @property
    @abstractmethod
    def power(self):
        pass

class WashingMachine(Appliance):
    @property
    def power(self):
        return '300W'

class Refrigerator(Appliance):
    @property
    def power(self):
        return '500W'

w = WashingMachine()
print(w.power)
r = Refrigerator()
print(r.power)

