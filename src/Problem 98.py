data = open("p098_words.txt", "r")

words, digit_num= [x.strip('"') for x in data.read().split(',')], 9

anagrams, words_copy = {}, words.copy()
for word in words_copy:
    for comp in words_copy:
        if len(word) == len(comp) and word != comp:
            w_list, c_list = [char for char in word], [char for char in comp]
            if sorted(w_list) == sorted(c_list):
                anagrams[word] = anagrams.get(word, []) + [comp]
                words_copy.remove(comp)

while digit_num == 9:
    print('word length: ', digit_num)
    wordlist = [(k, v[0]) for k, v in anagrams.items() if len(str(k)) == digit_num]

    print(wordlist)

    res, squares = 1, []
    while len(str(res ** 2)) < 10:
        squares.append(res ** 2)
        res += 1
    sq_list = [square for square in squares if len(str(square)) == digit_num]

    print('Sample size:', len(sq_list))

    for pair in wordlist:
        print(pair)
        sq_copy = sq_list.copy()
        while len(sq_copy) > 0:
            num1 = sq_copy.pop()
            trans = str.maketrans(str(num1), pair[0])
            for num2 in sq_copy:
                encode = str(num2).translate(trans)
                if encode == pair[1]:
                    print('Solution found: ', num1, num2, num1 ** 0.5, num2 ** 0.5, pair)
            if not len(sq_copy) % 1000:
                print(len(sq_copy))
    print('done')
    digit_num -= 1