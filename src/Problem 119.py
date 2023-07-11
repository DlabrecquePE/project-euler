def digit_sum(num):
    digit_list = [int(char) for char in str(num)]
    return sum(digit_list)

def gen_power_seq(n):
    a = 1
    while True:
        yield a ** n
        a += 1


a_list = []
for p in range(2, 50):
    sequence = gen_power_seq(p)
    term  = next(sequence)
    while term < 10:
        term = next(sequence)
    while True:
        term_length = len(str(term))
        max_s, max_term = 9 * term_length, 10 ** term_length
        max_s_to_p = max_s ** p
        diff = max_s_to_p - max_term
        digit_true_s = digit_sum(term)
        s_to_p = digit_true_s ** p
        if s_to_p == term:
            a_list.append(term)
        if max_s_to_p + diff < 0:
            break
        term = next(sequence)

a_list = sorted(a_list)
while len(a_list) > 30:
    a_list.pop()

print(a_list[-1])

        
