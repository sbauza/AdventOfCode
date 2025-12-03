
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def sum_digits(file):
    lines = read_file(file)
    _sum = 0

    for line in lines:
        line = line.rstrip('\n')
        max_joltage = 0
        numbers = list(map(int, list(line)))
        for idx, number in enumerate(numbers):
            if number * 10 < max_joltage:
                continue
            if len(numbers[idx+1:]) < 1:
                continue
            second_digit = max(numbers[idx+1:])
            joltage = int(str(number) + str(second_digit))
            if joltage > max_joltage:
                max_joltage = joltage
        _sum += max_joltage
    print(_sum)
    return _sum

assert 357 == sum_digits('test1.txt')
sum_digits('input.txt')
