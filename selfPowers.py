# Self powers (48)
#

def self_powers(n):
    return sum(i**i for i in range(1, n+1))


print(str(self_powers(1000))[-10:])

