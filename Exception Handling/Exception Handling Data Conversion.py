##Write a function that takes a list of strings and converts them to integers. Use try, except, and finally blocks to handle ValueError if a string cannot be converted and print an appropriate message.

def converter(lst):
    integer = []
    try:
        for i in lst:
          integer.append(int(i))
    except ValueError as e:
        print (e)
        integer = None
    finally :
        print("Program Executed")
    return integer

lst1 = ['1','2','3','4']
lst2 = ['1','a','2','3']

print(converter(lst1))
print(converter(lst2))
