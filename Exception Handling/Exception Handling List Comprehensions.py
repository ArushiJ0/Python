##Write a function that uses a list comprehension to convert a list of strings to integers. Use try, except, and finally blocks within the list comprehension to handle ValueError and print an appropriate message.

def lst_comp(lst):
    try:
        integer = [int(i) for i in lst]
    except ValueError as e:
        print(e)
        integer = None
    finally:
        print("Program Executed")
    return integer

lst1 = ['1','2','3']
lst2 = ['1','a','3']
print(lst_comp(lst1))
print(lst_comp(lst2))
