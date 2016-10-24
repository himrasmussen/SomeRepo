# Integer right triangles (39)
# Omkrets 840
# Perimiter 120

import time, pprint

# Omkrets
def upTo(n):
    for a in range(1, n):
        for b in range(a, n):
            if a + b > n:
                break
            for c in range(b, n):
                if a + b + c > n:
                    break
                if a**2 + b**2 == c**2:
                    solutions.setdefault(a+b+c, [])
                    solutions[a+b+c].append([a, b, c])

# Perimiter
def upTo2(n):
    for a in range(1, n):
        for b in range(a, n):
            if a * b / 2 > n:
                break
            for c in range(b, n):
                if a**2 + b**2 == c**2:
                    solutions.setdefault(a+b+c, [])
                    solutions[a+b+c].append([a, b, c])

startTime = time.time()
solutions = {}
upTo2(1000)


pprint.pprint(solutions)

most = 12
for key in solutions.keys():
    if len(solutions[key]) == '':
           continue
    if len(solutions[key]) > len(solutions[most]):
        most = key

print(most, solutions[most])
print(len(solutions[most]))
endTime = time.time()
print(endTime - startTime)

'''
none
240.15874004364014

a+b break
<= n
177.66521310806274

a+b break
a+b+c break
46.82104206085205

'''
