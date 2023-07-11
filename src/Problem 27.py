# Quadratic primes
# Problem 27
# Euler discovered the remarkable quadratic formula:
#
#   n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when
# n=40,40^2+40+41=40(40+1)+41n=40, is divisible by 41, and certainly
# when n=41,41^2+41+41n=41,41^2+41+41 is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values
# 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n^2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n=0.


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for x in range(2, int(num ** 0.5) + 1):
        if not num % x:
            return False
    return True

primes = [x for x in range(1001) if is_prime(x)]
neg_primes = [-x for x in range(1001) if is_prime(x)]

primes = primes + neg_primes

consecutive = []
for b in primes:
    for a in range(-999, 1000):
        index = 0
        while is_prime(index ** 2 + a * index + b):
            index += 1
        if index > 1:
            consecutive.append((a, b, index + 1))

test = []
for i in consecutive:
    test.append(i[2])

for j in consecutive:
    if j[2] == max(test):
        print(j[0]*j[1])
