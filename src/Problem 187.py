# Semiprimes
# Problem 187
# A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
#
# There are ten composites below thirty containing precisely two, not necessarily distinct,
# prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
#
# How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
from collections import deque


def prime_list(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


end, count = 10 ** 8, 0
prime_range = end // 2
prime_factors = deque(prime_list(prime_range))
while len(prime_factors) > 1:
    div = prime_factors.popleft()
    while len(prime_factors) > 0 and div * prime_factors[-1] > end:
        prime_factors.pop()
    if div ** 2 < end:
        count += len(prime_factors) + 1
print(count)
