# Counting summations
# Problem 76
# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?
from functools import lru_cache


@lru_cache(maxsize=2**30)
def coins(n, denoms):
    x = len(denoms)
    if n < 0 or x <= 0:
        return 0
    if n == 0:
        return 1
    removed, reduced = denoms[-1], denoms[:-1]
    return coins(n, reduced) + coins(n - removed, denoms)


for N in range(1, 101):
    denominations = tuple(range(1, N))
    print(N, coins(N, denominations))
