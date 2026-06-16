def Fibonacci(x , memo={}):
    if x in memo:
        return memo[x]
    if x<=1:
        return x
  
    memo[x] = Fibonacci(x-1, memo)+Fibonacci(x-2, memo)
    return memo[x]


print(Fibonacci(10))
print(Fibonacci(16))
print(Fibonacci(30))
