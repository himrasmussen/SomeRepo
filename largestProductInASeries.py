# Largest product in a series (8)
# 56184274944 index(731)

import os
os.chdir('C:\\Users\\PulseHealing\\Documents')

numberFile = open('Euler8.txt', 'r')

number = numberFile.readlines()[0]

biggest_product = 0

index = 0

for i in number:
    product = 1
    for n in number[index:index+13]:
        product *= int(n)
    if product > biggest_product:
        biggest_product = product
        biggest_product_index = index
    index += 1

print(str(biggest_product), str(biggest_product_index)) 
