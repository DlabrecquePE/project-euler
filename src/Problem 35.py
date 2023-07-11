# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are
# themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import json
data = open("primes less than 1 million.json", 'r')
primes = json.loads(data.read())


result = []
for elem in primes:
    prime_string = str(elem)
    pcheck = True
    test = [char for char in prime_string]
    for rotate in range(len(test)):
        mover = test.pop(0)
        test.append(mover)
        check = int(''.join(test))
        if check not in primes:
            pcheck = False
            break
    if pcheck:
        result.append(elem)
        print(elem)
print(len(result))
