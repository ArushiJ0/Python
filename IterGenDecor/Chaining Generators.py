def even_nums(n):
    for i in range (n+1):
        if i%2 ==0:
            yield i

def squares(n):
    for i in n :
        yield i**2

eve = even_nums(20)
sq = squares(eve)
for i in sq :
    print(i)
