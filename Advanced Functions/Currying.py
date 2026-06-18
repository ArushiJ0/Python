def num1(x):
    def num2 (y):
        def num3 (z):
            return x*y*z
        return num3
    return num2

print(num1(4)(5)(1))
