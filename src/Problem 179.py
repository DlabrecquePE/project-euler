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


def factorize(num, primes):
    """ Returns a list of prime factors of num """
    prime_factors, root_num = [], num ** 0.5
    for prime in primes:
        while not num % prime:
            prime_factors.append(prime)
            num = num // prime
        if num == 1:
            return sorted(prime_factors)
        if prime > root_num:
            return sorted(prime_factors + [num])


def divisor_num(num, primes):
    """ Returns the number of divisors from a list of prime factors """
    res, pfactors = 1, list(factorize(num, primes))
    for x in Counter(pfactors).values():
        res *= (x + 1)
    return res


primer = gen_primes()
prime, primes = next(primer), []
while prime <= max_n ** 0.5 + 1:
    primes.append(prime)
    prime = next(primer)

max_n, n, div_n, conseq_div_num = 10 ** 7, 1, 1, 0
while n < max_n:
    div_next_n = divisor_num(n + 1, primes)
    if div_n == div_next_n:
        conseq_div_num += 1
    n += 1
    div_n = div_next_n

print(conseq_div_num) 
    
# SLOW
