# Reciprocal cycles (26)
#

import decimal

decimal.getcontext().prec = 1000

help(decimal)

def reciprocal_cycle(n):
    cycle = str(decimal(1) / decimal(n))[2:]

    
