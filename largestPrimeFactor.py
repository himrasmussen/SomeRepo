# Largest prime factor (3)
# [71, 839, 1471, 6857]

import math

# Finds primes
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True

# Finds the largest prime factor
def largest_prime_factor(n):
    global prime_list
    global prime
    global gotAll
    prime_list = []
    for i in range(3, math.ceil(math.sqrt(n))):
        if prime(i):
            if n % i == 0:
                prime_list.append(i)
                print(prime_list)
                

def gotAll(n):
    global prime_list
    for i in prime_list[::-1]:
        if n % i == 0:
            continue
        else:
            print(str(n) + ' % ' + str(i) + ' = ' + str(n % i))
            break
    print('Found all prime factor. Largest prime factor is: ' + str(prime_list[-1]))
# Check if all prime factors are found
# For primes in factors[reversed]


largest_prime_factor(600851475143)


#600851475143
