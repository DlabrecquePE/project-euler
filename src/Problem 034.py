# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math as math


def digit_factorial(input_array):
    res = 0
    for i in range(len(input_array)):
        res += math.factorial(int(input_array[i]))
    return res


array = []
percent = 1
for x in range(10, 46448640):
    stringify = [char for char in str(x)]
    if x % 464486 == 0:
        print(percent, "percent complete")
        percent += 1
    if digit_factorial(stringify) == x:
        array.append(x)

print(sum(array))
