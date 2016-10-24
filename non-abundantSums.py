# Non-abundant sums
# 4151748



## Finn alle overflødige tall

abundant = []
for i in range(1, 28123):
    divisors = []
    for n in range(1, i):
        if i % n == 0:
            divisors.append(n)
    if sum(divisors) > i:
        abundant.append(i)

print(len(abundant))
print('\n', '-'*40, '\n')



sum_two_abundant = []
i = 1
# Finne alle tall som er summen av to overflødige tall

# Kjør linjene under like ofte som ting i "abundant" med a = ting1 første gang,
# a = ting2 andre gang etc.
for a in abundant:
    if i % 5 == 0:
        print(i)


    # For b i ting i abundant lik eller større enn a
    for b in abundant[abundant.index(a):]:

        # Stopp, gå opp til a og fortsett med neste i a hvis a + b er mer
        # enn 28123
        if a + b > 28123:
            break

        # Hvis a + b ikke er i sum_two_abuntant
        # legg til a + b i sum_two_abundant
        if a + b not in sum_two_abundant:
            sum_two_abundant.append(a + b)

    i += 1

print(sum(range(28123)) - sum(sum_two_abundant))





'''
not_two_abundant = []
for i in range(1, 28123 + 1):
    for n in abundant:
        if i - n < 0:
            not_two_abundant.append(i)
            break
        elif i - n in abundant:
            print(str(i) + ' = ' + str(i-n) + ' ' + str(n - 1))
            break
    not_two_abundant.append(i)
print(sum(not_two_abundant))'''
