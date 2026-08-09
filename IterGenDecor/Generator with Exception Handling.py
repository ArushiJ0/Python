def safe_divide(lst, div):
    for i in lst:
        try: 
            yield i/div
        except ZeroDivisionError:
            yield "Error"

lst = [1,2,3,4,5,6]
for i in safe_divide(lst, 2):
    print(i)

for i in safe_divide(lst, 0):
    print(i)


