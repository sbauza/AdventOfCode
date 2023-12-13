import re
import functools
import collections

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def value(hand):
    counts = sorted(collections.Counter(hand).values(), reverse=True)
    if 'J' in hand:
        joker_values = []
        for char in hand:
            if char != 'J':
                joker_values.append(value(hand.replace('J', char)))
        if joker_values:
            return max(joker_values)
    if counts[0] == 5:
        # Five of a kind
        return int(9e10)
    elif counts[0] == 4:
        # Four of a kind
        return int(8e10)
    elif counts[0] == 3 and counts[1] == 2:
        # Full house
        return int(7e10)
    elif counts[0] == 3 and counts[1] < 2:
        # Three of a kind
        return int(6e10)
    elif counts[0] == 2 and counts[1] == 2:
        # Two pairs
        return int(5e10)
    elif counts[0] == 2 and counts[1] < 2:
        # One pair
        return int(4e10)
    elif counts == [1, 1, 1, 1, 1]:
        # High card
        return int(3e10)

def value_if_identical(hand):
    # the latest is the highest card value
    order = 'J23456789TQKA'
    value = 0
    for idx, card in enumerate(hand):
        # let's use an hexadecimal base ;-)
        value += order.index(card) * 16**(4-idx)
    return value

def rules(a, b):
    handa, handb = a[0], b[0]
    if value(handa) > value(handb):
        return 1
    elif value(handa) < value(handb):
        return -1
    else:
        if value_if_identical(handa) > value_if_identical(handb):
            return 1
        elif value_if_identical(handa) < value_if_identical(handb):
            return -1
        else:
            return 0
    
def main(file):
    lines = read_file(file)
    def split(line):
        hand, bet = re.findall(r'\w+', line)
        return hand, int(bet)
        
    gambles = map(split, lines)
    total_winnings = 0
    for rank, (hand, bet) in enumerate(sorted(gambles,
                                              key=functools.cmp_to_key(rules)),
                                      start=1):
        total_winnings += rank * bet
    return total_winnings

assert 5905 == main('test.txt')
print(main('input.txt'))