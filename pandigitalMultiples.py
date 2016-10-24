# Pandigital multiples (38)
# 932718654

i = 1
biggest = 0

# Until the concataned product has more than 9 digits
while len(str(i) + str(i * 2)) < 10:
    num = ''
    n = 1

    # Concatanate the products of i * 1, i * 2...
    while len(num) == len(set(num)):
        num += str(i * n)
        n += 1

        # If the concatanated product is pandigital
        if set(num) == set('123456789'):
            if int(num) > biggest and len(num) == 9:
                biggest = int(num)
                print(biggest, i, n)
    i += 1



print('answer is:', biggest)
