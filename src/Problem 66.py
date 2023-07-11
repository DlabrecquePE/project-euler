# Diophantine equation
# Problem 66
# Consider quadratic Diophantine equations of the form:
#
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is
# square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:
#
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
# obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained.


def calc_cont_fract(seq):
    d, n = seq.pop(), 1
    while len(seq) > 1:
        n = d * seq.pop() + n
        d, n = n, d
    return seq.pop() * d + n, d


def gen_cont_frac_root(S):
    m, d, a0 = 0, 1, int(S ** 0.5)
    yield a0
    a = a0
    while True:
        m = d * a - m
        d = (S - m ** 2) // d
        a = (a0 + m) // d
        yield a


def gen_best_fraction_expansion_root(D):
    root = gen_cont_frac_root(D)
    a0, a1 = next(root), next(root)
    yield (a0, 1)
    yield (a0 * a1 + a0, a1)
    cont_fract_seq = [a0, a1]
    while True:
        cont_fract_seq.append(next(root))
        yield calc_cont_fract(cont_fract_seq.copy())


D_minimal_x = {}
for D in [x for x in range(2, 1000) if not (x ** 0.5).is_integer()]:
    expansions = gen_best_fraction_expansion_root(D)
    while True:
        x, y = next(expansions)
        if x ** 2 - D * (y ** 2) == 1:
            D_minimal_x[D] = x
            break
print(max(D_minimal_x, key=D_minimal_x.get))
