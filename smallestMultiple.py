# Smallest multiple (5)
# 232792560

n = 1
while True:
    for i in range(2, 21):
        found = True
        if n % i != 0:
            n += 1
            found = False
            break
    if found:
        print(str(n))
        break
    
