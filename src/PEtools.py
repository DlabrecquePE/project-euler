from functools import lru_cache
from collections import Counter


def list_product(nums):
    total = 1
    for num in nums:
        total *= num
    return total


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


def factorize(num):
    """ Returns a list of prime factors of num """
    prime_factors, primes, root_num = [num], gen_primes(), num ** 0.5
    for prime in primes:
        while not num % prime:
            prime_factors.append(prime)
            num = num // prime
        if num == 1:
            return sorted(prime_factors)
        # if prime > root_num:
        #     return sorted(prime_factors)


def divisor_num(num):
    """ Returns the number of divisors from a list of prime factors """
    res, pfactors = 1, list(factorize(num))
    print(pfactors)
    for x in Counter(pfactors).values():
        res *= (x + 1)
    return res


def is_prime(num):
    """ Test for primality """
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for x in range(3, int(num ** 0.5) + 1, 2):
        if not num % x:
            return False
    return True


@ lru_cache(maxsize=2**18)
def collatz_chain(n):
    """ Returns list with collatz chain starting at n """
    if n == 1:
        return [1]
    if n % 2:
        return [n] + collatz_chain(3 * n + 1)
    else:
        return [n] + collatz_chain(n // 2)


@lru_cache(maxsize=2**18)
def collatz_chain_length(n):
    """ Returns an the integer number of elements in thh collatz chain of n """
    if n == 1:
        return 1
    if n % 2:
        return collatz_chain_length(3 * n + 1) + 1
    else:
        return collatz_chain_length(n // 2) + 1


def is_palindrome(n):
    """ Determines if n is palindromic (read the same back to front) """
    n_str = str(n)
    n_len = len(n_str)
    a, b = n_str[:n_len//2], n_str[:-n_len//2]
    if a == b:
        return True
    return False


def bico(num):
    """ Returns list of binomial coefficients in
        the terms of the polynomial expansion of
        the binomial power (x + 1) ** n"""
    
    from math import factorial

    return [factorial(num) // (factorial(k) * factorial(num - k)) for k in range(num + 1)]
      