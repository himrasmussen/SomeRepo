# Pentagon numbers (44)
# 22

# First Pk - Pj = Px


def makePenta(n):
    return n * (3 * n - 1) // 2


penta = []

for i in range(1, 100):
    penta.append(makePenta(i))



lowest = 100
for a in range(len(penta)):
    for b in range(a+1, len(penta)-a):
        if penta[b] - penta[a+1] in penta and penta[b] - penta[a+1] < lowest:
            print(penta[b], penta[a+1], ':', penta[b] - penta[a+1])
            lowest = penta[b] - penta[a+1]

    

