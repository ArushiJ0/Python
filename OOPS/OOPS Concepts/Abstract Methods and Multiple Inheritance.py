from abc import ABC , abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineer")

class Doctor(Worker):
    def work(self):
        print("Doctor")

class Scientist(Engineer, Doctor):
    def work(self):
        Engineer.work(self)
        Doctor.work(self)

s = Scientist()
s.work()
