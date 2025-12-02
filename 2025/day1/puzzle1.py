
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def sum_digits(file):
    lines = read_file(file)
    pos = 50
    sum = 0
    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        move = int(line[1:])
        pos = (pos + direction * move) % 100
        print(pos)
        if pos == 0:
            sum += 1
    print(sum)
    return sum

assert 3 == sum_digits('test1.txt')
sum_digits('input.txt')
