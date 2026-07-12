## Write a function that calls another function which may raise an exception. Use try, except, and finally blocks to handle the exception and print an appropriate message.

def fun1():
    raise Exception ("Error Occurred")

def fun2():
    try:
        fun1()
    
    except Exception as e:
        print(e)

    finally:
        print("Program Executed")

print(fun2())
