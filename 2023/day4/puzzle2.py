import re
from collections import defaultdict

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)
    cards = defaultdict(int)
    for line in lines:
        line = line.rstrip('\n')
        win_numbs = set()
        actual_numbs = set()
        _card, _win_numbs, _actual_numbs = re.split('[:|\|]', line)
        card = int(re.findall('\d+', _card)[0])
        cards[card] += 1
        for _numb in re.finditer('\d+', _win_numbs):
            win_numbs.add(int(_numb.group()))
        for _numb in re.finditer('\d+', _actual_numbs):
            actual_numbs.add(int(_numb.group()))
        actual_win_numbs = actual_numbs.intersection(win_numbs)
        wins = len(actual_win_numbs)
        if actual_win_numbs:
            for next_card in range(card+1, card+wins+1):
                cards[next_card] += cards[card]
    return sum(cards.values())

assert 30 == main('test.txt')
print(main('input.txt'))