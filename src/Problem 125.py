def is_palindrome(num):
    num_str = str(num)
    num_len = len(num_str)
    a = num_str[:num_len//2]
    b = num_str[(num_len+1)//2:]
    if a == b[::-1]:
        return True
    return False


a, squares, max_n = 1, [], 10 ** 8
a_sq = a ** 2
while a_sq < max_n:
    squares.append(a_sq)
    a += 1
    a_sq = a ** 2

palindromes = []
for i, sq in enumerate(squares[:-1]):
    count = i + 1
    total = sq + squares[count]
    while total < max_n:
        count += 1
        if is_palindrome(total):
            palindromes.append(total)
        total += squares[count]
print(sum(list(set(palindromes))))
