# Singular integer right triangles
   
# Problem 75

# It turns out that 12 cm is the smallest length of wire 
# that can be bent to form an integer sided right angle 
# triangle in exactly one way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent 
# to form an integer sided right angle triangle, and other lengths 
# allow more than one solution to be found; for example, using 120 
# cm it is possible to form exactly three different integer sided 
# right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values 
# of L ≤ 1,500,000 can exactly one integer sided right angle 
# triangle be formed?
from collections import Counter

n, m, trip, per, max_per, triples = 1, 2, [3, 4, 5], 0, 1500000, set()
while per <= max_per:
    while per <= max_per:
        k = 1
        while True:
            triple = [k * i for i in trip]
            k += 1
            if sum(triple) >= max_per:
                break
            else:
                triples.add(tuple(triple))
        m += 1
        trip = sorted([m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2])
        per = sum(trip)
    n += 1
    m = n + 1
    trip = sorted([m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2])
    per = sum(trip)

c = Counter()
c.update([sum(i) for i in triples])
print(len([x for x, y in c.items() if y == 1]))
