# Goldbach's other conjecture
# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
# a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if not num % index:
            return False
    return True


primes = [2]
x = 3

while True:
    flag = False
    if is_prime(x):
        flag = True
        primes.append(x)
    else:
        square_check, s = 0, 1
        while 2 + 2 * s ** 2 <= x and square_check != x:
            for prime in primes:
                square_check = prime + 2 * s ** 2
                if square_check == x:
                    flag = True
                    break
            s += 1
    if not flag:
        print(x)
        break
    x += 2