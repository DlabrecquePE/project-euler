# Coin partitions
# Problem 78
# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five
# coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.
from functools import lru_cache


def pent_num(num):
    return num * (3 * num - 1) // 2


@lru_cache(maxsize=2**30)
def part(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    k_range = int(((24 * num + 1) ** 0.5 + 1) / 6)
    k_range = [i for i in range(-k_range, k_range + 1) if i]
    p_sum = 0
    for k in k_range:
        coef = (-1) ** (abs(k) - 1)
        p_sum += coef * part(num - pent_num(k))
    return p_sum

N, x = 1000000, 0
while True:
    if not part(x) % N:
        print(x)
        break
    x += 1
