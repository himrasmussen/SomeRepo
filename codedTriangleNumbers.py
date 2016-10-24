# Coded triangle numbers (42)
#

import os

os.chdir('C:\\Users\\PulseHealing\\Documents\\')


words = []
triangle_numbers = []

for i in range(100000):
    triangle = i * (i + 1) // 2
    triangle_numbers.append(triangle)

with open('coded_triangle_numbers.txt') as f:
    for line in f.read().splitlines():
        words.append(line)

a = string.ascii_lowercase

tot = 0

for word in lines:
    wsum = 0
    for letter in word:
        wsum += a.index(letter)
    if wsum in triangle_numbers:
        tot += 1

print(tot)
