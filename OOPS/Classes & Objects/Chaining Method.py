##Create a class named `Calculator` with methods to add, subtract, multiply, and divide. Each method should return the object itself to allow method chaining. Create an object and chain multiple method calls.

class Calculator:
    def __init__(self, value =0):
        self.value = value

    def add(self,num):
        self.value += num
        return self

    def sub (self, num):
        self.value -= num
        return self

    def mul (self, num):
        self.value *= num
        return self

    def div (self, num):
        if num ==0 :
            print("Cannot divide")
        else:
            self.value /=  num
            return self

c = Calculator()
c.add(50).sub(5).mul(10).div(2)
print(c.value)

        
