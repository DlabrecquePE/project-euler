import numpy as np

u_n, u_n_seq = 1, []
for n in range(1, 11):
    u_n += n ** 2 + n ** 4 + n ** 6 + n ** 8 + n ** 10
    u_n -= n + n ** 3 + n ** 5 + n ** 7 + n ** 9
    u_n_seq.append(u_n)
print(u_n_seq)
 
