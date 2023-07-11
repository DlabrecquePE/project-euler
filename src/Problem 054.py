def poker_value(hand):
    rank_table, hand_value = str.maketrans('TJQKA', 'abcde'), 0
    ranks = list(reversed(sorted([elem[0].translate(rank_table) for elem in hand])))
    suits, unique = set(elem[1] for elem in hand), set(ranks)
    unique_rank = len(unique)

    if unique_rank == 5:                # Test for high card / flush / straight
        if len(suits) == 1:
            hand_value += 5
        if int(ranks[0], 16) - int(ranks[4], 16) == 4:
            hand_value += 4
        r_result = ranks.copy()
    elif unique_rank == 4:              # Test for one pair
        hand_value = 1
        pair_rank = ranks.copy()
        for elem in unique:
            pair_rank.remove(elem)
        r_result = pair_rank * 2 + [elem for elem in ranks if elem not in pair_rank]
    elif unique_rank == 3:              # Test for two pair / three of a kind
        tok_test = [len(set(ranks[x:x+3])) for x in range(3)]
        if 1 in tok_test:
            hand_value = 3
            r_result = [ranks[2]] * 3 + [elem for elem in ranks if elem != ranks[2]]
        else:
            hand_value = 2
            r_result = [ranks[1]] * 2 + [ranks[3]] * 2 + [elem for elem in ranks if elem not in [ranks[1], ranks[3]]]
    elif unique_rank == 2:              # test for full house / four of a kind
        if ranks[1] == ranks[3]:
            hand_value = 7
            r_result = [ranks[1]] * 4 + [elem for elem in ranks if elem != ranks[4]]
        else:
            hand_value = 6
            r_result = [ranks[2]] * 3 + [elem for elem in ranks if elem != ranks[2]]
    return int(''.join([str(hand_value)] + r_result), 16)


f, p1_wins = open('data/p054_poker.txt', 'r'), 0
f1 = f.readlines()
for hand in f1:
    cards = hand.split()
    player1, player2 = cards[:5], cards[5:]
    value1, value2 = poker_value(player1), poker_value(player2)

    if value1 > value2:
        p1_wins += 1
print(p1_wins)
f.close()
