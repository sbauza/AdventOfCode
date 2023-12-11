
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def sum_digits(file):
    lines = read_file(file)
    sum = 0
    for line in lines:
        first = ''
        last = ''
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in reversed(line):
            if char.isdigit():
                last = char
                break
        sum += int(first + '' + last)
    print(sum)
    return sum

assert 142 == sum_digits('test.txt')
sum_digits('input.txt')