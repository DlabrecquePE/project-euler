from PEtools import gen_primes

limit = 10 ** 10
primer = gen_primes()
for n, p_n in enumerate(primer):
    p_n_sq = p_n ** 2
    r = (pow(p_n - 1, n + 1, p_n_sq) + pow(p_n + 1, n + 1, p_n_sq)) % p_n_sq
    if r > limit:
        print(n + 1)
        break

    
