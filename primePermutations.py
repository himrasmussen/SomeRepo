# Prime permutations (49)
# 125925919521

import itertools

def sieve(limit):
    numbers = list(range(2, limit+1))
    primes = []

    for i in numbers:
        for m in numbers[numbers.index(i)+1:]:
            if m % i == 0:
                numbers.remove(m)


    return numbers


prime_list = sieve(10000)

for i in prime_list[prime_list.index(997):]:
    permutations = 0
    primes = []
    for perm in itertools.permutations(str(i)):
        if int(''.join(perm)) in prime_list:
            permutations += 1
            primes.append(''.join(perm))
    if permutations == 3:
        print(''.join(sorted(primes)))
        break
