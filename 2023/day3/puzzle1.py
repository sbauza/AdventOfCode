import math
import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def is_symbol(char):
    return not char.isalnum() and char != '.'

def main(file):
    sum_hits = 0
    hits = []
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
                if is_symbol(line[index]):
                    hits.append(number)
                    break
                if row > 0 and is_symbol(lines[row-1][index]):
                    hits.append(number)
                    break
                if row < line_max and is_symbol(lines[row+1][index]):
                    hits.append(number)
                    break
    sum_hits = sum(hits)
    return sum_hits

assert 4361 == main('test.txt')
print(main('input.txt'))