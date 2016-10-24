# Summation of primes (10)
# 142913828922

prime_list = []

def prime(n):
    for i in prime_list:
        if n % i == 0:
            return False
            break
    return True

for i in range(2, 2*10**6 + 1):
    if prime(i):
        prime_list.append(i)
        print(str(i))

print(str(sum(prime_list)))

        
