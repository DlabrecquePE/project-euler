# Integer right triangles
# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
# solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

triples = []
for k in range(1, 251):
    for m in range(1, 251):
        for n in range(m + 1, 251):
            a = k * (n ** 2 - m ** 2)
            b = k * (2 * m * n)
            c = k * (n ** 2 + m ** 2)
            if a + b + c <= 1000 and a ** 2 + b ** 2 == c ** 2:
                triples.append((a, b, c))
                print(a, b, c)

perimeters = [sum(tri) for tri in set(triples)]
print(max(perimeters, key=perimeters.count))
