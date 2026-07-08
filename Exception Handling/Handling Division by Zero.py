##Write a function that takes two integers as input and returns their division. Use try, except, and finally blocks to handle division by zero and print an appropriate message.

def DivZero(a,b):
   try :
         ans = a/b
   except ZeroDivisionError as e:
       print(e)
       print('Enter number greater than 0')
       ans = None 
   finally :
      print('Program executed')
   return ans
   
print(DivZero(8,0))
