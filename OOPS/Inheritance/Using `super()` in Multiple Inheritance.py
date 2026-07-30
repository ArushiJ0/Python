class Person :
    def __init__(self,name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person , Employee):
    def __init__(self, name, employee_id):
        super().__init__(name)
        Employee.__init__(self, employee_id)

m = Manager('Rahul', 241)
print(m.name, m.employee_id)
