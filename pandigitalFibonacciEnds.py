# Pandigital Fibonacci Ends (104)
# 329467
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order). And F2749,
which contains 575 digits, is the first Fibonacci number for which the
first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
'''

#import sys

def test_if_condition(num):
    num = str(num)
    for i in [str(i) for i in range(1, 10)]:
        if i not in set(num[:9]):
            return False
        if i not in set(num[-9:]):
            return False
    return True

i = 1
a, b = 0, 1
while True:
    b, a = a+b, b
    if test_if_condition(b):
        print(a, b, i)
        break
    if i % 15000 == 0:
        print(i)
    i += 1
