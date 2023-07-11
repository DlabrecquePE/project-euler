# Prime power triples
# Problem 87
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact,
# there are exactly four numbers below fifty that can be expressed in such a way:
#
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime
# fourth power?


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if not num % index:
            return False
    return True


primes = [2]
for x in range(3, 7072):
    if is_prime(x):
        primes.append(x)

results = []
for k, z in enumerate(primes[:86]):
    for j, y in enumerate(primes[:369]):
        for i, x in enumerate(primes):
            summation = x ** 2 + y ** 3 + z ** 4
            if summation < 50000000:
                results.append(summation)
print(len(set(results)))
