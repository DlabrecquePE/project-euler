# Highly divisible triangular number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?
from collections import Counter


def gen_primes():
    """ Generate an infinite sequence of prime numbers """
    d, q = {}, 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


def factorize(num, primes=gen_primes()):
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
        if prime > num ** 0.5:
            return prime_factors + [num]


p_range, primer = 10000, gen_primes()
prime, prime_array = next(primer), []
while prime <= p_range:
    prime_array.append(prime)
    prime = next(primer)

max_div, n = 0, 1
div1 = []
while(max_div < 501 and n < p_range ** 2):
    div2, divnum = factorize(n + 1, prime_array), 1
    div_total = sorted(div1 + div2)
    for x in Counter(div_total[1:]).values():
        divnum *= x + 1
    if divnum > max_div:
        max_div = divnum
        print(n, ': ', (n * (n + 1)) // 2, ' ', divnum)
    div1, n = div2, n + 1
print(n - 1, (n * (n - 1)) // 2)
