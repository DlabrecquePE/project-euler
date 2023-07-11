# Prime summations
# Problem 77
# It is possible to write ten as the sum of primes in exactly five different ways:
#
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
#
# What is the first value which can be written as the sum of primes in over five thousand different ways?
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


@lru_cache(maxsize=2 ** 8)
def is_prime(num):
    return not (num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)))


def gen_prime(num=2**32):
    step, count = 3, 0
    yield 2
    while True:
        if is_prime(step):
            yield step
            count += 1
        if count >= num:
            break
        step += 2


N = 5000
primes, number, maxpartitions = gen_prime(), 1, 1
prime_denoms = next(primes),
while True:
    if number > max(prime_denoms):
        prime_denoms = (*prime_denoms, next(primes))
    partitions = coins(number, prime_denoms)
    if partitions >= N:
        print(number)
        break
    number += 1
