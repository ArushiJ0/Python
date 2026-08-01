from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
        
    def calculate_salary(self):
        print(f"Full Time Salary:{self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, salary , per_hours):
        self.salary = salary
        self.per_hours = per_hours
        
    def calculate_salary(self):
        print(f"Part Time Salary{self.salary*self.per_hours}")

f = FullTimeEmployee(6000)
p = PartTimeEmployee(800, 12)
f.calculate_salary()
p.calculate_salary()
