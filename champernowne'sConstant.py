# Champernowne's constant (40)
# 210



c = ''
for i in range(1, 1000001):
    c += str(i)

product = 1
for i in range(0, 7):
    product *= int(c[10**i-1])

print(product)
