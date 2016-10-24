# 1000-digit Fibonacci number (25)
# 4782

def fib_up_to_digits(n):
    a, b, index = 0, 1, 1
    while len(str(b)) != n:
        a, b = b, a+b
        index += 1
        print(len(str(b)))
    return index

print(fib_up_to_digits(1000))
