# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

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


def pfactor(num):
    """ Returns a dict of prime factors of num          """
    """ dict keys are the prime factors                 """
    """ values contain the number of factors (exponent) """

    prime_factors, primes = {}, gen_primes()
    for prime in primes:
        while not num % prime:
            prime_factors[prime] = prime_factors.get(prime, 0) + 1
            num = num // prime
        if num == 1:
            return prime_factors
        if prime > num ** 0.5:
            prime_factors[num] = 1
            return prime_factors


def divisors(num):
    """ takes a dict of prime factors from pfactor()    """
    """ returns list of divisors                        """

    num_dict = pfactor(num)

    def inner_divisors(num_dict, num_list={1}):
        if not num_dict:
            return num_list

        prime = min(num_dict.keys())
        exp = num_dict[prime]
        del num_dict[prime]
        back_list = inner_divisors(num_dict, num_list)
        work_list = [prime ** (i + 1) for i in range(exp)]
        for div in work_list:
            num_list = num_list.union(x * div for x in back_list)
        num_list = num_list.union(work_list).union(back_list)
        return num_list

    return sorted(list(inner_divisors(num_dict)))

max_N = 10 ** 5

s = {x: sum(divisors(x)[:-1]) for x in range(2, max_N)}
am = {x: y for x, y in s.items() if 1 < x < y < max_N and s[y] == x}
print(sum(list(am.keys()) + list(am.values())))

print(s)
