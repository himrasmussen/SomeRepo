# Sub-string divisibility (43)
# 16695334890

import itertools
import time

startTime = time.time()

def tupleConc(*args):
	return ''.join(args)

def checkDiv(n):
    for i in range(1, 8):
        if int(n[i:i+3]) % prime[i-1] != 0:
            return False
            break
    return True


##def tupleConc(a, b, c):
##	return str(a) + str(b) + str(c)


prime = [2, 3, 5, 7, 11, 13, 17]

num = '0123456789'


tempPermutations = list(itertools.permutations(num))

permutations = list(itertools.starmap(tupleConc, tempPermutations))

#print(permutations)

trueNums = list(filter(checkDiv, permutations))

print(trueNums)
print(sum(list(map(lambda x: int(x), trueNums))))
endTime = time.time()

print(endTime - startTime)
