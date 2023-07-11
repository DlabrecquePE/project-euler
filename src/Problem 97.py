# Large non-Mersenne prime
# Problem 97
# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
# 2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1,
# have been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.
#
# Find the last ten digits of this prime number.


def draw_progress_bar(percent, barlen=20):
    import sys

    sys.stdout.write("\r")
    progress = ""
    for i in range(barlen):
        if i < int(barlen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
    sys.stdout.flush()


total = 28433
for x in range(7830457):
    total = total << 1
    if not x % 10000:
        draw_progress_bar(x / 7830457)
total += 1

print(str(total)[-10:])
