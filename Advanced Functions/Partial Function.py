from functools import partial

def partial_fun(x,y):
    return x*y

result = partial(partial_fun,2)
print(result(3))
print(result(6))
