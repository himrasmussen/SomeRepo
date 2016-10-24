# Highly divisiable triangle number (12)
#

import sys


i = 3075
most_divisors = 0
while True:
    i += 1
    divisors = 0
    triangle = sum(list(range(1, i + 1)))
    print(str(triangle), str(i))
    for n in range(1, triangle + 1):
        if triangle % n == 0:
            divisors += 1
    if divisors > most_divisors:
        most_divisors = divisors
        print(str(most_divisors) + ' divisors')
    if divisors > 500:
        print(str(triangle) + ' has over 500 divisors.')
        sys.exit()




#i = 4240
#288, 3135
