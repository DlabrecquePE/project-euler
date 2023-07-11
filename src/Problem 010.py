# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

data = open("Primes Below 2 Million.txt", "r")
sum_array = [int(lines.rstrip('\n')) for lines in data.readlines()]

print(sum(sum_array))
