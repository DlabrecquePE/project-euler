from PEtools import gen_primes
from collections import defaultdict
from itertools import islice

prime_concat = defaultdict(list)
arr = list(islice(gen_primes(), 1, 1000))

for i, prime in enumerate(arr):
    print(prime)
    for conc in arr[i+1:]:
        string1 = str(prime) + str(conc)
        string2 = str(conc) + str(prime)
        if string1 in arr or string2 in arr:
            prime_concat[prime] = prime_concat[prime].append(conc)
print(list(prime_concat))
