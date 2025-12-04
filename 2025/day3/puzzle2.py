
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


from itertools import islice

def find_max_substr(digits, k):
    n = len(digits)
    if k > n:
        return digits

    result = []
    start = 0

    from functools import reduce

    def picker(acc, _):
        result, start, i = acc
        remaining_needed = k - i - 1
        end = n - remaining_needed
        window = list(islice(digits, start, end))
        if not window:
            return (result, start, i)  # No change
        max_digit, max_idx = max(((digit, idx) for idx, digit in enumerate(window)), key=lambda x: x[0])
        result = result + [max_digit]
        start = start + max_idx + 1
        return (result, start, i + 1)

    result, start, _ = reduce(picker, range(k), ([], 0, 0))

    return result


def sum_digits(file):
    lines = read_file(file)
    _sum = 0
    k = 12  # Number of digits to pick

    for line in lines:
        line = line.rstrip('\n')
        numbers = list(map(int, list(line)))
        
        max_substr = find_max_substr(numbers, k)
        max_joltage = int(''.join(map(str, max_substr)))
        
        _sum += max_joltage
    print(_sum)
    return _sum

assert 3121910778619 == sum_digits('test1.txt')
sum_digits('input.txt')
