# Powerfull digit sum (56)
# 972

max_sum = 0
for i in range(1, 100):
    for n in range(1, 100):
        if sum(int(i) for i in str(i**n)) > max_sum:
            max_sum = sum(int(i) for i in str(i**n))

print(str(max_sum))
