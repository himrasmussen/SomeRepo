# Lychrel numbers (55)
# 249

import pprint

def isLychrel(n):
    #n = n
    for i in range(50):
        m = str(n)
        n += int(m[::-1])
        m = str(n)
        if str(n) == m[::-1]:
            return True
            break
    return False

lychrel = []

for i in range(1, 10001):
    if not isLychrel(i):
        lychrel.append(i)

pprint.pprint(lychrel)
print(len(lychrel)) 
print()
for i in lychrel:
    if str(i) == str(i)[::-1]:
        print(i)

