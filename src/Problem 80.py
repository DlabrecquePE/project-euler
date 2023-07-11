# Square root digital expansion
# Problem 80
# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
# expansion of such square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal
# digits is 475.
#
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
# for all the irrational square roots.
from decimal import *

getcontext().prec = 102
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

total = 0
for x in range(100):
    if x not in squares:
        root = Decimal(x).sqrt()
        parsed = str(root).replace('.', '')[:100]
        digits = [int(char) for char in parsed]
        total += sum(digits)
print(total)
