# Spiral primes
# Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If
# this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?


def prime_list(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def is_prime(num):
    for prime in prime_divisors:
        if prime > int(num ** 0.5):
            break
        if not num % prime:
            return False
    return True


def gen_ullam_corners(sidelength=3):
    k, j, value = 1, 1, 0
    while True:
        batch = set()
        value = 4 * k ** 2 + 1
        while value < sidelength ** 2:
            batch.add(value)
            k += 1
            value = 4 * k ** 2 + 1
        value = j ** 2 + j + 1
        while value < sidelength ** 2:
            batch.add(value)
            j += 1
            value = j ** 2 + j + 1
        yield batch
        sidelength += 2


c_gen = gen_ullam_corners()
prime_divisors = prime_list(32768)
side, p_count = 3, 0
while True:
    c_list = set(next(c_gen))
    for elem in c_list:
        if is_prime(elem):
            p_count += 1
    percentage = p_count / (2 * side - 1)
    if percentage < 0.1:
        print(side)
        break
    side += 2
