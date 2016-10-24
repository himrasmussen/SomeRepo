# Prime power triples (87)

import prime as p

pL = p.sieve(7100)
print(pL[0], pL[-1])

usums = []

for p1 in pL:
    print(p1)
    if p1**2 > 50000000:
        break
    for p2 in pL:
        if p1**2 + p2**3 > 50000000:
            break
        for p3 in pL:
            if p1**2 + p2**3 + p3**4 > 50000000:
                break
            elif p1**2 + p2**3 + p3**4 not in usums:
                usums.append(p1**2 + p2**3 + p3**4)

print(len(usums))
