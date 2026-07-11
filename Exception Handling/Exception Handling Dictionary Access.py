##Write a function that takes a dictionary and a key as input and returns the value associated with the key. Use try, except, and finally blocks to handle KeyError if the key is not found in the dictionary and print an appropriate message.

def func(dct,key):
    try:
        value = dct[key]
    except KeyError as e:
        print(e)
        print("Error Occurred")
        value = None 
    finally:
        print("Program Executed")
    return value

Dict = {'a':1,'b':2,'c':3}
print(func(Dict,'c'))
print(func(Dict,'e'))
            
