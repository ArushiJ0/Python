def uppercase(func):
    def wrapper(*args, **kwargs):
        upper = func(*args, **kwargs)
        return upper.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        ex = func(*args, **kwargs)
        return ex + "!"
    return wrapper



@uppercase
@exclaim
def msg(msg):
    return msg

print(msg("hello"))
