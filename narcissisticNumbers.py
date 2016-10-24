# Narcissistic Numbers
# [
#  153, 370, 371, 407, 1634, 8208,
#  9474, 54748, 92727, 93084, 548834
#  1741725, 4210818, 9800817, 9926315
# ]

# The number is equal to the sum of its digits raised to the power of number
# of digits

def narNum(i):
    value = 0
    for n in str(i):
        value += int(n)**len(str(i))

    if i == value:
        return True
    else:
        return False


        #sum + map


##def narNum2(i):
##    print(sum(map(lambda x: x**len(str(i)), str(i))))

print(narNum2(153))

narNums = []
i = 1
while True:
    if narNum(i):
        narNums.append(i)
        print(narNums)
    i += 1
