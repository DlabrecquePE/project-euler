# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import sys
from functools import lru_cache

sys.setrecursionlimit(2000)


@lru_cache(maxsize=2**16)
def coins(n, denoms):
    x = len(denoms)
    if n < 0 or x <= 0:
        return 0
    if n == 0:
        return 1
    removed, reduced = denoms[-1], denoms[:-1]
    return coins(n, reduced) + coins(n - removed, denoms)


denominations = (1, 2, 5, 10, 20, 50, 100, 200)
N = 200
print(coins(N, denominations))
