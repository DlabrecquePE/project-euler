# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def _stringify(num):
    string_array = [char for char in str(num)]
    return string_array


def _sum_fifth(input_array):
    total = 0
    for i in input_array:
        total += int(i) ** 5
    return total


from time import time

start = time()
fp_digits = []
for x in range(10, 1000000):
    if sum([int(char) ** 5  for char in str(x)]) == x:
        fp_digits.append(x)
print(sum(fp_digits))
print(time() - start)