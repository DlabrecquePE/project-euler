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


def factorize(num, primes):
    """ Returns a list of prime factors of num """
    prime_factors, max_prime = set(), int(num ** 0.5) + 1
    for prime in primes:
        while not num % prime:
            prime_factors.add(prime)
            num = num // prime
            if num == 1:
                return prime_factors
        if prime >= max_prime:
            # print(prime)
            return list(prime_factors)


def totient(num, primes):
    factors = factorize(num, primes)
    numers, denoms = [x - 1 for x in factors], [x for x in factors]
    l_numers, l_denoms = list_product(numers), list_product(denoms)
    return (num * l_numers) // l_denoms

prime, d, R = gen_primes(), 2, 1
p_list = [next(prime)]
while R >= 14599 / 94744:
    while d > p_list[-1]:
        p_list.append(next(prime))
    if d not in p_list:
        R = totient(d, p_list) / (d - 1)
    if not d % 100000:
        print(d)
    d += 1
print('Found: d=', d, ' with R(d) value: ', R)
