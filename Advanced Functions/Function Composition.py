def function(f ,g):
    result = lambda x:f(g(x))
    return result

def f(x):
    y = x-1
    return y
def g(y):
    return y*2

val = function(f,g)
print(val(4))
