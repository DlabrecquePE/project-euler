# Prime permutations
# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two
# ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but
# there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if not num % divisor:
            return False
    return True


primes = []
for x in range(1001, 10000, 2):
    if is_prime(x):
        primes.append(x)

perm_dict = {}
for i, x in enumerate(primes):
    first_perm = sorted([int(char) for char in str(x)])
    for y in primes[i + 1:]:
        second_perm = sorted([int(char) for char in str(y)])
        if second_perm == first_perm:
            z = 2 * y - x
            third_perm = sorted([int(char) for char in str(z)])
            if z in primes and third_perm == first_perm and x != 1487:
                print(str(x) + str(y) + str(z))
