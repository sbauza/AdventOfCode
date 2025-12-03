
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def find_max_substr(digits, k):
    n = len(digits)
    if k > n:
        return digits
    
    result = []
    start = 0
    
    for i in range(k):
        remaining_needed = k - i - 1
        end = n - remaining_needed
        
        max_digit = -1
        max_pos = start
        for pos in range(start, end):
            if digits[pos] > max_digit:
                max_digit = digits[pos]
                max_pos = pos
        
        result.append(max_digit)
        start = max_pos + 1
    
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
