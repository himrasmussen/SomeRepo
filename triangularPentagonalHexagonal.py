# Triangular, pentagonal, and hexagonal (45)
# 1533776805

def Tri(n):
    return n * (n + 1) // 2

def Pen(n):
    return n * (3 * n - 1) // 2

def Hex(n):
    return n * (2 * n - 1)

Tria, Pent, Hexa = [], [], []



for i in range(2, 100000):
    Tria.append(Tri(i))
    Pent.append(Pen(i))
    Hexa.append(Hex(i))
print(Tria.index(1533776805), Pent.index(1533776805), Hexa.index(1533776805))
print(set(Tria) & set(Pent) & set(Hexa))

#print Tri if Tri is Pen and Hex and not 40755
