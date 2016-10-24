# Factorial digit sum (18)
# 648?

def sum_of_digits_in_factorial(n):
    sum_of_digits_in_factorial = 0
    prod = 1
    for i in range(n, 0, -1):
        prod *= i
    for i in str(prod):
        sum_of_digits_in_factorial += int(i)
    return sum_of_digits_in_factorial

print(str(sum_of_digits_in_factorial(100)))
