def generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

calculate =generator()
for _ in range(10):
    print(next(calculate))


