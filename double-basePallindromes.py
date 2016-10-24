# Double-base pallindromes (36)
# 872187

def pallindrome(i):
    if str(i) == str(i)[::-1]:
        return True
    else:
        return False



pallindromes = []

for i in range(1, 1000001):
    if pallindrome(i):
        if pallindrome(bin(i)[2:]):
            pallindromes.append(i)

print(str(sum(pallindromes)))
print(str(pallindromes))
