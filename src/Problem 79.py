# Passcode derivation
# Problem 79
# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
# would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
# possible secret passcode of unknown length.

data = open('data/p079_keylog.txt', 'r')
keylogs = []
for line in data.readlines():
    keylogs.append([int(char) for char in line.strip('\n')])

result = []
while len(keylogs) > 0:
    head_nums, tail_nums = set(), set()
    for log in keylogs.copy():
        if len(log) > 0:
            head_nums.add(log[0])
        if len(log) > 1:
            tail_nums.add(log[1])
        if len(log) > 2:
            tail_nums.add(log[2])
    first_numeral = head_nums.difference(tail_nums).pop()
    for i, log in enumerate(keylogs.copy()):
        if len(log) > 0 and log[0] == first_numeral:
            del keylogs[i][0]
    result.append(first_numeral)
    keylogs = [x for x in keylogs if x != []]
print(''.join([str(x) for x in result]))
