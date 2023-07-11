def gen_r(a):
    n, a_sq = 1, a ** 2
    a_dec, a_inc = a - 1, a + 1
    while True:
        yield (pow(a_dec, n, a_sq) + pow(a_inc, n, a_sq))%a_sq
        n += 2


r_max = []
for a in range(3, 1001):
    r = gen_r(a)
    r_seq = []
    while True:
        r_seq += [next(r), next(r)]
        if r_seq[:len(r_seq)//2] == r_seq[len(r_seq)//2:]:
            r_max.append(max(r_seq))
            break
print(sum(r_max))
