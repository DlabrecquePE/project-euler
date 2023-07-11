# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import json
data = open('primes less than 1 million.json', 'r')
primes = json.load(data)

conseq, end_result = 21, []
while True:
    results, offset, conseq_sum = [], 0, 0
    while conseq_sum < 1000000:
        conseq_sum = sum(primes[offset: conseq+offset])
        if conseq_sum in primes:
            results.append((offset, conseq, sum(primes[offset: conseq+offset])))
        offset += 1
    if len(results) == 1:
        end_string = str(results[0][2])+', a sum of '+str(conseq)+' primes starting at '+str(primes[results[0][0]])
    if sum(primes[:conseq]) > 1000000:
        print(end_string)
        break
    conseq += 2
