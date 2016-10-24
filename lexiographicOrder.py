# Lexiographic permutations (24)
# '2', '7', '8', '3', '9', '1', '5', '4', '6', '0'

import itertools

def tupleConc(*args):
    return ''.join(args)



permutations = []
for i in itertools.permutations('0123456789'):
    permutations.append(i)
    if len(permutations) == 1000000:
        print(str(permutations[999999]))
