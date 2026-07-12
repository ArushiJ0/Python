##Define a class with a method that performs a division operation. Use try, except, and finally blocks within the method to handle division by zero and print an appropriate message.

class Division: 
    def  divide (self,a,b):
        try:
            return a/b
        except ZeroDivisionError as e:
            print (e)
            return None
        finally:
            print("Program Executed")
    
d = Division()
print(d.divide(3,0))

print(d.divide(6,3))
