fib = (lambda n: n if n <= 1 else fib(n-1) + fib(n-2))

# test the function
n=int(input("enter"))
print([fib(i) for i in range(n)])
