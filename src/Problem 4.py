# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
candidates, n = [], 3

for a in range(10 ** n - 1, 10 ** (n - 1) - 1, -1):
    for b in range(a, 10 ** (n - 1) - 1, -1):
        test = str(a * b)
        if test == test[::-1]:
            candidates.append(int(test))
print(max(candidates))
