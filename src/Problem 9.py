# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import numpy as np

root_array=[]

for n in range (0,1000):
    r=np.roots([1,n,-1000])
    root_array.append(r)

for i in root_array:
    if root_array[i,0].is_integer() and root_array[i,1].is_integer()

root_array

# I ended up working this out by hand a=375 b=200 c=425 with abc=31875000
