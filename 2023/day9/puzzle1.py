import re
import itertools

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)
    sum_hits = []
    for line in lines:
        last_nums = []
        history = list(map(int, re.findall(r'[-]?\w+', line)))
        while set(history) != {0}:
            last_nums.append(history[-1])
            history = list(map(lambda x: x[1] - x[0], itertools.pairwise(history)))
        sum_hits.append(sum(last_nums))
    return sum(sum_hits)

assert 114 == main('test.txt')
print(main('input.txt'))