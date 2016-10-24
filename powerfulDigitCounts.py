# Powerful digit counts (63)
# 49


result = []

for i in range(1, 1000):
    for n in range(1, 1000):
        if len(str(i**n)) == n:
            result.append(i**n)

print(len(result))
