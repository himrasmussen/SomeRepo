# Distinct powers (29)
# 9183

distinct_powers = []

for i in range(2, 101):
    for n in range(2, 101):
        if i**n not in distinct_powers:
            distinct_powers.append(i**n)

print(str(len(distinct_powers)))
