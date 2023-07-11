# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

factorize_this = 600851475143


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


def factorize(n):
    """ Returns a list of prime factors of n """
    primer, factors, p_stop = gen_primes(), [], int(n ** 0.5) + 1
    prime = next(primer)
    while True:
        if not n % prime:
            factors.append(prime)
            while not n % prime:
                n = n // prime
                if prime >= n:
                    return factors
        if prime > p_stop:
            return factors + [n]
        prime = next(primer)


res = factorize(factorize_this)
print(max(res))
