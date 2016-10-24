# Sum square difference
# 25164150

squares = [i**2 for i in range(1, 101)]
numbers = [i for i in range(1, 101)]

print(str(sum(squares) - (sum(numbers)**2)))
