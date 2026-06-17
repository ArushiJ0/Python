def Error (x=None):
    try:
        return (sum(x)/len(x))
    except ZeroDivisionError:
        return None
    
L1=[1,2,3,4,5]
L2=[]

print(Error(L1))
print(Error(L2))

