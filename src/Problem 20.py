# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math

string = str(math.factorial(100))

factorial_sum = 0
for i in range(len(string)):
    factorial_sum += int(string[i])

print(factorial_sum)
