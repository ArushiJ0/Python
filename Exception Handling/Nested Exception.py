##Write a function that performs nested exception handling. It should first attempt to convert a string to an integer, and then attempt to divide by that integer. Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.

def nested (a, div):
    try:
        value = int(a)
        try:
            ans = value/div
        except ZeroDivisionError as e:
            print(e)
            value = None
            ans = None
        finally:
            print("2nd loop executed")
    except ValueError  as e:
        print (e)
        ans = None
    finally:
       print ("1st loop executed")
    return ans

print(nested('8',4))
print (nested('str',2))
print(nested('6',0))

        
