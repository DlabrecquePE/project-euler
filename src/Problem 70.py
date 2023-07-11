#%% 
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


def factorize(num, primes=gen_primes()):
    """ Returns a list of prime factors of num """
    prime_factors, max_prime = [], int(num ** 0.5) + 1
    for prime in primes:
        while not num % prime:
            prime_factors.append(prime)
            num = num // prime
            if num == 1:
                return prime_factors
        if prime >= max_prime:
            # print(prime)
            return [num] + prime_factors


def totient(num, primes=gen_primes()):
    factors = factorize(num, primes)
    numers, denoms = [x - 1 for x in factors], [x for x in factors]
    l_numers, l_denoms = list_product(numers), list_product(denoms)
    # print(num, numers, denoms, l_numers, l_denoms)
    return num * l_numers // l_denoms

#%% 
print('calculating primes...')
primer, max_n, p_list = gen_primes(), 10 ** 7, []
prime = next(primer)
while prime < max_n ** 0.5 + 1:
    p_list.append(prime)
    prime = next(primer)

#%% 
print('calculating totients...')
totients = {}
for n in range(2, max_n):
    totients[n] = totient(n, (n for n in p_list))
    if not n % 10 ** 5:
        print(n // 10 ** 5, ' percent')

print('testing permutations...')
tester, solutions = {x: p_list[x] for x in range(10)}, {}
for n, t in totients.items():
    n_digits = [tester[int(char)] for char in str(n)]
    t_digits = [tester[int(char)] for char in str(t)]
    if list_product(n_digits) == list_product(t_digits):
        solutions[n] = t
    if not n % 10 ** 5:
        print(n // 10 ** 5, ' percent')
print('found ', len(solutions), ' solutions')

print('finding minimum...')
ratios = {}
for k, v in solutions.items():
    ratios[k] = k / v
print(min(ratios, key=ratios.get))




