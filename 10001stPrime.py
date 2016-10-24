# 10001st prime
# 104743

def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True

def nth_prime(n):
    prime_list = []
    for i in range(2, 10*10**1000000):
        if prime(i):
            prime_list.append(i)
            if len(prime_list) == n:
                return(prime_list[n-1])

print(nth_prime(10001))
