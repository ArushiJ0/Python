def function():
    def func(x):
        return x**2
    return func
square =function()
print(square(4))
print(square(8))
print(square(3))

