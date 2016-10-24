# Number spiral diagonals (28)
#

import pprint


# while limx and limy <= 1001
# go right 1 more than limx, and add one to limx, place i and add one to i,
# go down one more than limy and add one to limy, place i and add one to i,
# go left one more than limx, add one to limx, place i and add one to i,
# go up one more than limy, add one to limy, place i and add one to i,
# etc

# until pointer is at limx:
    # move right, place i, add 1 to i
# increase limx with 1

# until pointer is at -limy:
    # move down, place i, add 1 to i

# until pointer is at -limx:
    # move left, place i, add 1 to i

# until pointer is at limy:
    # move up, place i, add 1 to i
# increase limy with 1



grid = {(0, 0): 1}

# Sets limits
limx, limy = 0, 0

# pointer
cx, cy = 0, 0

tot = 0

i = 1


while limx <= 2 and limy <= 2:

    # Move right
    cx += 1
    grid[cx, cy] = i
    i += 1
    limx += 1
    tot += grid[cx, cy]
    print(grid[cx, cy])
    while cx < limx:
        cx += 1
        grid[cx, cy] = i
        i += 1



    # Move down
    if grid[cx, cy] != 2:
        tot += grid[cx, cy]
        print(grid[cx, cy])
    cy -= 1
    grid[cx, cy] = i
    i += 1
    limy += 1
    while cy > -limy:
        cy -= 1
        grid[cx, cy] = i
        i += 1

    if limx > 2 or limy > 2:
        break

    # Move left
    cx -= 1
    grid[cx, cy] = i
    i += 1
    tot += grid[cx, cy]
    print(grid[cx, cy])
    while cx > -limx:
        cx -= 1
        grid[cx, cy] = i
        i += 1

    # Move up
    cy += 1
    grid[cx, cy] = i
    i += 1
    tot += grid[cx, cy]
    print(grid[cx, cy])
    while cy < limy:
        cy += 1
        grid[cx, cy] = i
        i += 1


print(tot, cx, cy)
