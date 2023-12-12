from collections import defaultdict
import math
import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def is_gear(char):
    return char == '*'

def add_number_to_gear(gears, gear, number):
    if len(gears[gear]) < 2:
        gears[gear].append(number)
    else:
        print('too many numbers for gear %s: %s' % (gear, gears[gear]))
        gears[gear] = []
        
def main(file):
    gears = defaultdict(list)
    sum_hits = 0
    lines = read_file(file)
    line_max = len(lines) - 1
    for row, line in enumerate(lines):
        line = line.rstrip('\n')
        pos_max = len(line) - 1
        numbers = re.finditer(r'(\d+)', line)
        for number_ in numbers:
            number = int(number_.group())
            start, end = number_.span()
            for index in range(max(0, start -1), min(end + 1, pos_max +1)):
                if is_gear(line[index]):
                    add_number_to_gear(gears, (row, index), number)
                    break
                if row > 0 and is_gear(lines[row-1][index]):
                    add_number_to_gear(gears, (row-1, index), number)
                    break
                if row < line_max and is_gear(lines[row+1][index]):
                    add_number_to_gear(gears, (row+1, index), number)
                    break
    print(gears)
    for k, v in gears.items():
        if len(v) == 2:
            sum_hits += math.prod(v)
    return sum_hits

assert 467835 == main('test.txt')
print(main('input.txt'))