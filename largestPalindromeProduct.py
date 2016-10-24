# Largets palindrome product (4)
# 906609, (993, 913)

biggest = 0
numbers = ()

for i in range(1000, 101, -1):
    for n in range(i, 101, -1):
        if str(i*n) == str(i*n)[::-1]:
            if i*n > biggest:
                biggest = i*n
                numbers = (i, n)

print(biggest)
print(numbers)

