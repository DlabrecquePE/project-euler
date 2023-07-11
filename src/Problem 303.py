from time import time

timer = time()
res, max_n = [], 10000
for n in range(max_n):
    print(n + 1)
    m = n + 1
    while True:
        parse = [int(char) for char in str(m)]
        if all(num in [0, 1, 2] for num in parse):
            res.append(m // (n + 1))
            break
        else:
            m += n + 1
print(sum(res))
print(time() - timer)
