# Amicable numbers (21)
# 31626

def d(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

amicable_numbers = []
def amicable(a):
    global amicable_numbers
    b = d(a)
    if a != b and d(b) == a:
        if a not in amicable_numbers:
            amicable_numbers.append(a)
        if b not in amicable_numbers:
            amicable_numbers.append(b)
        print(str(a), str(b))
        
for i in range(1, 10001):
    amicable(i)

print(str(amicable_numbers))
print(str(sum(amicable_numbers)))

