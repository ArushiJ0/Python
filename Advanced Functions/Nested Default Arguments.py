def Function(a,b=None):
    if b is None:
        b={}
        
    b[a]=a**2
    return b

print(Function(3))

print(Function(3,{1:1,2:4}))
