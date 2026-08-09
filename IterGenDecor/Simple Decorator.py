
import time 
def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time:{end -start}")
        return result
    return wrapper

    

@time_it
def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(28))
