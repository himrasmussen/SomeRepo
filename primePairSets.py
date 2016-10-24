# Prime pair sets (60)
#

import itertools

import prime as p

prime_list = p.prime_list()

for prime1 in prime_list:
    for prime2 in prime_list:
        for a in itertools.permutations([str(prime1), str(prime2)], 2):
            if int(''.join(a)) not in prime_list:
                break

        for prime3 in prime_list:
            for b in itertools.permutations([str(prime1), str(prime2),\
                                             str(prime3)], 2):
                if int(''.join(b)) not in prime_list:
                    break

            for prime4 in prime_list:
                for c in itertools.permutations([str(prime1), str(prime2),\
                                                 str(prime3), str(prime4)], 2):
                    if int(''.join(c)) not in prime_list:
                        break

                for prime5 in prime_list:
                    for p in itertools.permutations([str(prime1), str(prime2),\
                                                     str(prime3), str(prime4),\
                                                     str(prime5)], 2):
                        if int(''.join(p)) not in prime_list:
                            break

                    for p in itertools.permutations(reversed([str(prime1), str(prime2),\
                                                     str(prime3), str(prime4),\
                                                     str(prime5)], 2)):
                        if int(''.join(p)) not in prime_list:
                            break

                    sum_set = sum[prime1, prime2, prime3, prime4, prime]
                    print(sum_set)
                    if sum_set < lowest:
                        lowest = sum_set
                        print('lowest:', sum_set)
