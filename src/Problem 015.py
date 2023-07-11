# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

import math as math

array = []
for n in range(1, 21):
    array.append(int(math.factorial(2*n)/math.factorial(n)**2))

print(array)
