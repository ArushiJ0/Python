##Write a function that takes a list of integers and returns their sum. Use try, except, and finally blocks to handle TypeError if a non-integer value is encountered and print an appropriate message.

def int_sum(lst):
    try:
        add = sum(lst)
        return add
    except TypeError as e:
        print (e)
        add = None 
    finally:
        print('Execution Completed')

lst = [9 , 8 , 7 , 0]
lst2 = [9,0,8,7,'a']

print(int_sum(lst))
print(int_sum(lst2))
