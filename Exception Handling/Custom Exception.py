##Define a custom exception named `NegativeNumberError`. Write a function that raises this exception if a negative number is encountered in a list. Use try, except, and finally blocks to handle the custom exception and print an appropriate message.

class NegativeNumberError(Exception):
    pass

def neg(lst):
    try:
        for i in lst:
            if  i < 0:
                raise NegativeNumberError ("This list contains a negative number")
    except NegativeNumberError as e:
        print (e)
    finally :
        print("Program Executed")

lst = [1,2,3,-9,0]
print(neg(lst))
