# Consecutive prime sum (50)
# 997651 543

import os
os.chdir('C:\\Users\\PulseHealing\\Documents')
#primeFile = open('primeFile.txt')



def prime(n):
    for i in primes:
        if n % i == 0:
            return False
            break
    return True


'''
primes = []
primes.append(primeFile.readlines().split('\n'))
'''
primes = []

for i in range(2, 1000001):
    if prime(i):
        primes.append(i)


print()


greatest_sum = 0
# Startindex primtall
i = -1
consecutive = 0
for i in range(10):
    # Sluttindex primtall
    n = i+1
    # Ny startindex primtall
    i += 1
    # 
    while sum(primes[i:n]) < 1000001:
        if sum(primes[i:n]) in primes:
            # n-i er antall påfølgende primtall
            if n-i > consecutive:
                greatest_sum = sum(primes[i:n])
                consecutive = n-i
                print('longest consecutive', consecutive, greatest_sum)
                

        
        if i == len(primes)-1:
            break

        # Ny sluttindex primtall
        n += 1

print(greatest_sum, consecutive)

#primeFile.close()
