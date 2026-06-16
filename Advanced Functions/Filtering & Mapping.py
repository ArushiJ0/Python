def Function(f,m,List):
    L = [m(x) for x in List if f(x)]
    return L

print(Function(lambda x:x%2==0 , lambda x:x**2 ,[1,2,3,4,5]))
