from functools import lru_cache


@lru_cache(maxsize=2 ** 8)
def is_prime(num):
    return not (num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)))


def gen_prime(num):
    step, count = 3, 0
    yield 2
    while True:
        if is_prime(step):
            yield step
            count += 1
        if count >= num:
            break
        step += 2


primes = list(gen_prime(16))
n_local_minima, totient_local_minima, product, a = [], [], 1, 1
for prime in primes:
    product *= prime
    a *= prime - 1
    n_local_minima.append(product)
    totient_local_minima.append(a)

totient_dict = dict(zip(n_local_minima, totient_local_minima))


N = 1000000
for x in sorted(list(totient_dict.keys()))[::-1]:
    if x <= N:
        print(x)
        break