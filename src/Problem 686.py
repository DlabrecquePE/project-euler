import math

L = '123'
n = 678910
log_term = math.log10(2)
j_list = []

j = 1
while True:
    nlog = j * log_term
    short = str(10 ** (nlog - math.floor(nlog) + 2))
    if short[:3] == L:
        j_list.append(j)
    ntest = len(j_list)
    if ntest == n:
        print(j, 'is the solution')
        break
    j += 1
    if ntest % 10000 == 0:
        print(ntest)