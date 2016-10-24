# Digit factorials (34)
# 40730

def factorial(n):
    value = 1
    for i in range(1, n+1):
        value *= i
    return value

digit_factorial_numbers = []

for i in range(3, 10000001):
    digit_factorial = 0
    for n in str(i):
        digit_factorial += factorial(int(n))
    if digit_factorial == i and i not in digit_factorial_numbers:
        digit_factorial_numbers.append(i)


print(str(sum(digit_factorial_numbers)))
