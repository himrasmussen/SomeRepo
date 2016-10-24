# Permutated multiples (52)
# 142857

123456
i = 1
while True:
    if set(i*1) == set(i*2) == set(i*3) == \
       set (i*4) == set(i*5) == set(i*6):
        print(i)
        break
    i += 1
    if i % 3000 == 0:
        print(i)



# print i if sets for i*1 through i*6 are equal
