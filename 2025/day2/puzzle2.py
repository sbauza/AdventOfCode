from collections import deque
import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def sum_digits(file):
    lines = read_file(file)
    _sum = 0

    for line in lines:
        for _range in line.rstrip('\n').split(','):
            if _range == '':
                continue
            min, max = (int(i) for i in _range.split('-') if i.isdigit())
            numbers = list(filter(lambda x: re.match(r'^(\d+)\1+$', str(x)), range(min, max+1)))
            _sum += sum(numbers)
    print(_sum)
    return _sum

assert 4174379265 == sum_digits('test1.txt')
sum_digits('input.txt')
