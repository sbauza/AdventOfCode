import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    sum_hits = 0
    lines = read_file(file)
    for line in lines:
        line = line.rstrip('\n')
        win_numbs = set()
        actual_numbs = set()
        _card, _win_numbs, _actual_numbs = re.split('[:|\|]', line)
        card = int(re.findall('\d+', _card)[0])
        for _numb in re.finditer('\d+', _win_numbs):
            win_numbs.add(int(_numb.group()))
        for _numb in re.finditer('\d+', _actual_numbs):
            actual_numbs.add(int(_numb.group()))
        actual_win_numbs = actual_numbs.intersection(win_numbs)
        if actual_win_numbs:
            points = pow(2, len(actual_win_numbs) - 1)
            sum_hits += points
    return sum_hits

assert 13 == main('test.txt')
print(main('input.txt'))