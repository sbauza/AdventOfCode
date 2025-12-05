
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def get_fresh_and_available(lines):
    fresh = []
    available = []
    on_available = False
    for line in lines:
        line = line.rstrip('\n')
        if not on_available:
            min_max = line.split('-')
            if len(min_max) != 2:
                on_available = True
            else:
                fresh.append((int(min_max[0]), int(min_max[1])))
        else:
            available.append(int(line))
    return fresh, available

def is_fresh(avail_fruit, fresh):
    for fresh_range in fresh:
        if avail_fruit >= fresh_range[0] and avail_fruit <= fresh_range[1]:
            return True
    return False

def sum_digits(file):
    lines = read_file(file)
    fresh, available = get_fresh_and_available(lines)
    _sum = 0

    for avail_fruit in available:
        _sum += is_fresh(avail_fruit, fresh)
    print(_sum)
    return _sum

assert 3 == sum_digits('test1.txt')
sum_digits('input.txt')
