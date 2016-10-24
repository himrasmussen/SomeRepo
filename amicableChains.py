# Amicable chains (95)
#

def d(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)


def amicable(a):
    global amicable_numbers
    b = d(a)
    if a != b and d(b) == a:
        if a not in amicable_numbers:
            amicable_numbers.append(a)
        if b not in amicable_numbers:
            amicable_numbers.append(b)
        print(str(a), str(b))

def find_chain(limit):
    for i in range(220, limit+1):
