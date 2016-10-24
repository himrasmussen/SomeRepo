# Truncable primes (37)
# 748317

import math


primeList = [2]
truncable_primes = []

# Checks n for prime
def prime(n):
    upperLimit = 0
    #while upperLimit < math.sqrt(n):
    #    upperLimit = next(iter(primeList))

    # Set upper limit for divisor search
    for i in primeList:
        if i > math.sqrt(n):
            upperLimit = i
            break

    # Do divisor search
    for i in primeList[:primeList.index(upperLimit)+1]:
        if n % i == 0:
            # Divisor found, n is not prime
            return False
            break
    # No divisor found, n is prime
    return True


# Checks if n is a truncable prime
def truncable_prime(n):
    n = str(n)


    #
    for j in range(len(n)):
        # 3, 73, 373
        if int(n[j:]) not in primeList:
            return False


    #
    for k in range(len(n)):
        # 3, 37, 373..
        if int(n[:k+1]) not in primeList:
            return False


    #
    return True


for i in range(3, 1000000):
    if prime(i):
        primeList.append(i)

print('Done')


# Primes under 7 are by definition not truncable primes

for prime in primeList:

    if prime in [2, 3, 5, 7]:
        continue

    if len(truncable_primes) == 11:
        break

    if truncable_prime(prime):
        truncable_primes.append(prime)
        print('New truncable prime:', prime)


print(str(truncable_primes))
print(sum(truncable_primes))
