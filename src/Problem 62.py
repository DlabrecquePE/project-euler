# Cubic permutations
# Problem 62
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

cubes = {}
for x in range(10000):
    digits = [int(char) for char in str(x ** 3)]
    cubes[x] = sorted(digits)

for x in cubes:
    count = 0
    for y in cubes.values():
        if cubes[x] == y:
            count += 1
    if count == 5:
        print(x ** 3)
        break
