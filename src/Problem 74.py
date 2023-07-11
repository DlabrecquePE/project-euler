# Digit factorial chains
# Problem 74
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
# that there are only three such loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
# number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from math import *


def digit_factorial(num):
    digit_string = [factorial(int(char)) for char in str(num)]
    return sum(digit_string)


result = []
for x in range(1000000):
    if not x % 10000:
        print(x // 10000,'percent complete')
    index = 0
    chain_test = x
    while chain_test not in [digit_factorial(chain_test), 169, 363601, 1454, 871, 872, 45361, 45362]:
        index += 1
        chain_test = digit_factorial(chain_test)
    if index > 56:
        if chain_test == 169 or index == 58:
            result.append(x)

print(result)
print(len(result))
