# Cubic permutations (62)
# 127035954683

cubes = {i: ''.join(sorted(str(i**3))) for i in range(300000)}

cubes_list = []

for k, v in sorted(cubes.items()):
    cubes_list.append(v)


most = 0

for index, cube in enumerate(cubes_list):
    current = cubes_list.count(cube)
    if current > most:
        most = current
        most_index = index
        print(most, most_index)

print(most, most_index)
