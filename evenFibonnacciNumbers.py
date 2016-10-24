# Even Fibonacci numbers (2)
# 4613732

def fib(n):
    fib_list = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        if b % 2 == 0:
            fib_list.append(b)
    return(fib_list)

print(sum(fib(4*10**6)))



