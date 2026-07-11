##Write a function that takes a list and an index as input and returns the element at the given index. Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.
def list_error (lst, index):
    try :
        value =  lst[index] 
    except IndexError as e:
        print(e)
        value = None
    finally:
        print("Program Executed")
    return value

lst = [1,2,3,4,5]
print(list_error(lst, 0))
print(list_error(lst, 7))
