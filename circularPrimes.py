# Circular primes
#

import itertools

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    else:
        return True

primes = []
for i in range(1, 100001):
    if prime(i):
        primes.append(i)

for prime in primes:
    for i in permutations(prime):
        if not prime(i):
            break
    circular_primes.append(prime)

print(str(len(circular_primes)))
