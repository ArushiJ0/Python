def func(func_callback,List):
    return [func_callback(x)for x in List]


print(func(lambda x:x+1,[1,2,3,4,5]))
