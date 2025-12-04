
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def get_map(lines):
    map = []
    for line in lines:
        line = line.rstrip('\n')
        map.append(list(line))
    return map

def is_available(map, row, col):
    rolls = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
                continue
            if map[i][j] == '@':
                rolls += 1
    return rolls < 4

def sum_digits(file):
    lines = read_file(file)
    map = get_map(lines)
    _sum = 0
    for row, line in enumerate(map):
        for col, char in enumerate(line):
            if char == '@':
                if is_available(map, row, col):
                    _sum += 1
    print(_sum)
    return _sum

assert 13 == sum_digits('test1.txt')
sum_digits('input.txt')
