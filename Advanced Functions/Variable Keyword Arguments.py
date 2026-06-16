def variable_number(**kwargs):
    integers =list(filter(lambda x: isinstance(x,int),kwargs.values()))
    return integers
var ={'a':6, 'b':'x','c':9,'d':1,'e':'egg'}
print(variable_number(**var))
    
    
