##Create a class named `MathOperations` with a static method to calculate the square root of a number. Call the static method without creating an object.

import math 
class MathOperations:
    @staticmethod
    def sqroot(n):
        return math.sqrt(n)
    
ans = MathOperations.sqroot(5)
print(ans)
        
        
