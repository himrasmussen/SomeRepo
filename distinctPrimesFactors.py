# Distinct primes factors (47)
#

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True



def prime_factors(n):
    prime_factors = []
    for i in prime_list:
        if i > n:
            break
        if n % i == 0:

            # Finds the power of i
            temp_n = n
            power = []
            while temp_n % i == 0:
                power.append(i)
                temp_n = temp_n // i

                if temp_n % i != 0:
                    power = tuple(power)
                    prime_factors.append(power)
                    break

            prime_factors.append(i)

    return prime_factors



prime_list = [2]

# Generate primes up to 2000
for i in range(3, 2000):
    if prime(i):
        prime_list.append(i)


print(prime_factors(4))

'''
n = 1
while True:
    # Four consecutive numbers can't share prime factors.
    # Therefore the length of the set of all common prime factors between
    # The four numbers must be 0
    if len(set(prime_factors(n)) & \
           set(prime_factors(n+1)) & \
           set(prime_factors(n+2)) & \
           set(prime_factors(n+3))) \
           == 0:
           print(i)
           print(prime_factors(n), \
                  prime_factors(n+1), \
                  prime_factors(n+2), \
                  prime_factors(n+3))
           break
    n += 1
'''
