# Distinct primes factors
# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
#
# eventually found at 134043


def prime_factor_expansion(num):
    data = dict()
    for x in range(2, num // 2  + 1):
        while not num % x:
            if x not in data:
                data[x] = 1
            else:
                data[x] += 1
            num = num // x
    return data

order = 4
index = 129000
while True:
    expansion = []
    for x in range(order):
        factors = [tuple(y) for y in prime_factor_expansion(index + x).items()]
        expansion += factors
    if len(expansion) == order ** 2:
        print('found number at index:', index)
        break
    print(index, len(expansion))
    index += 1
