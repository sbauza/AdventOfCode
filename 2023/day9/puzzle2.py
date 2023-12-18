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
        first_nums = []
        history = list(map(int, re.findall(r'[-]?\w+', line)))
        while set(history) != {0}:
            first_nums.append(history[0])
            history = list(map(lambda x: x[1] - x[0], itertools.pairwise(history)))
        calculated_firsts = list(itertools.accumulate(
            reversed(first_nums), lambda x, y: y - x))
        sum_hits.append(calculated_firsts[-1])
    print(sum(sum_hits))
    return sum(sum_hits)

assert 2 == main('test.txt')
print(main('input.txt'))