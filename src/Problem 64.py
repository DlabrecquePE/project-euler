# All square roots are periodic when written as continued fractions and can be written in the form:
#
# √N = a0 + [1 / a1 + [1 / a2 + [1 / a3 + ...
# For example, let us consider √23:
#
# √23 = 4+√23—4 = 4 + 1/[1/(√23-4)] = 4+1/[1+(√23-3)/7]
#
# If we continue we would get the following expansion:
#
# √23 = 4+[1+[1/[3+1/[1+(8+...
#
# The process can be summarised as follows:
# 
# a0 = 4
# a1 = 1
# a2 = 3
# a3 = 1
# a4 = 8
# a5 = 1
# a6 = 3
# a7 = 1
#
# It can be seen that the sequence is repeating. For conciseness,
# we use the notation √23 = [4;(1,3,1,8)], to indicate that the
# block (1,3,1,8) repeats indefinitely.
#
# The first ten continued fraction representations of (irrational)
# square roots are:
#
# √2=[1;(2)], period=1
# √3=[1;(1,2)], period=2
# √5=[2;(4)], period=1
# √6=[2;(2,4)], period=2
# √7=[2;(1,1,1,4)], period=4
# √8=[2;(1,4)], period=2
# √10=[3;(6)], period=1
# √11=[3;(3,6)], period=2
# √12= [3;(2,6)], period=2
# √13=[3;(1,1,1,1,6)], period=5
#
# Exactly four continued fractions, for N ≤ 13, have an odd period.
#
# How many continued fractions for N ≤ 10000 have an odd period?

# %%
def cont_frac_root_repeating(S):
    m, d, a0, repeat = 0, 1, int(S ** 0.5), []
    a = a0
    while a != 2 * a0:
        m = d * a - m
        d = (S - m ** 2) // d
        a = (a0 + m) // d
        repeat.append(a)
    return repeat


# %%
N, count = 10000, 0
for x in [y for y in range(2, N + 1) if not (y ** 0.5).is_integer()]:
    if len(cont_frac_root_repeating(x)) % 2:
        count += 1
print(count)
