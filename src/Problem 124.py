# Ordered radicals
# Problem 124
#
# The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so
# rad(504) = 2 × 3 × 7 = 42.
#
# If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values
# are equal, we get:
#
#         Unsorted                    Sorted
#         n       rad(n)          n       rad(n)  k
#         1       1               1       1       1
#         2       2               2       2       2
#         3       3               4       2       3
#         4       2               8       2       4
#         5       5               3       3       5
#         6       6               9       3       6
#         7       7               5       5       7
#         8       2               6       6       8
#         9       3               7       7       9
#         10      10              10      10      10
#
# Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
#
# If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).


def prime_list(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def factorize(num, primes):
    """ Returns a list of prime factors of num """
    if not float(num).is_integer() or num < 1:
        raise Exception("Error: Can only factorize positive integers.")
    prime_factors = []
    for prime in primes:
        while not num % prime:
            prime_factors.append(prime)
            num = num // prime
        if num == 1:
            return prime_factors


prime, rads = prime_list(100000), []
for x in range(1, 100001):
    dpf = set(factorize(x, prime))
    product = 1
    for y in dpf:
        product *= y
    rads.append((product, x))
rads = sorted(rads)
print(rads[9999][1])