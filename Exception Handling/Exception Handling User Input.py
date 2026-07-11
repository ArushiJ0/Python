##Write a function that prompts the user to enter an integer. Use try, except, and finally blocks to handle ValueError if the user enters a non-integer value and print an appropriate message.

def user_input():
    try:
        a = int(input('Enter a number'))
    except ValueError as e:
        print(e)
        a = None 
    finally:
        print("Program Executed")
    return a

print(user_input())
