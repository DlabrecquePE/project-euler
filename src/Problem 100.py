# Arranged probability
   
# Problem 100

# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
# and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
# P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
# is a box containing eighty-five blue discs and thirty-five red discs.

# By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, 
# determine the number of blue discs that the box would contain.

#%%
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


#%%
i = gen_best_fraction_expansion_root(2)
j = next(i)
while j[0] < 2 * 10 ** 12 -1:
    j = next(i)  
#%%
print((j[1] + 1) // 2)

#%%
