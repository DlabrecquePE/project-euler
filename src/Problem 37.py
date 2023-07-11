# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if not num % index:
            return False
    return True


primes = [2, 3, 5, 7]
x = 11
result = []
while True:
    if is_prime(x):
        primes.append(x)
        x_string = str(x)
        left_trunc = [int(x_string[index + 1:]) for index in range(len(x_string) - 1)]
        right_trunc = [int(x_string[:index + 1]) for index in range(len(x_string) - 1)]
        trun_list = left_trunc + right_trunc
        if all(elem in primes for elem in trun_list):
            result.append(x)
    if len(result) == 11:
        print(sum(result))
        break
    x += 2
