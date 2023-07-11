# Pandigital prime
# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from itertools import *


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    else:
        return True


perm_array = []
for i in permutations("1234567", 7):
    string = ""
    for j in range(len(i)):
        string = string + i[j]
    perm_array.append(int(string))

prime_array = []
for i in perm_array:
    if is_prime(i):
        prime_array.append(i)

print(max(prime_array))
