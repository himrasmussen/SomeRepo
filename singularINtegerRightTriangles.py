# Singular integer right triangles (75)
#


def upTo(n):
    solutions = {}
    for a in range(1, n):
        if a % 5 == 0:
            print(a)
        #print(a)

        for b in range(a, n):
            if a + b > n:
                break


            for c in range(b, n):
                if a + b + c > n:
                    break
                elif a**2 + b**2 < c**2:
                    break

                elif a**2 + b**2 == c**2:
                    solutions.setdefault(a+b+c, [])
                    solutions[a+b+c].append([a, b, c])


    return solutions

solutions = upTo(1500000 + 1)

tot = 0
for i in solutions.values():
    if len(i) == 1:
        tot += 1

print(tot)
