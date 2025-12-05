
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def get_fresh_ranges(lines):
    fresh = []
    for line in lines:
        line = line.rstrip('\n')
        min_max = line.split('-')
        if len(min_max) != 2:
            break
        fresh.append((int(min_max[0]), int(min_max[1])))
    if not fresh:
        return fresh
    ranges = sorted(fresh, key=lambda x: x[0])
    merged = []
    for min_val, max_val in ranges:
        if not merged:
            merged.append((min_val, max_val))
        else:
            last_min, last_max = merged[-1]
            if min_val <= last_max + 1:
                merged[-1] = (last_min, max(last_max, max_val))
            else:
                merged.append((min_val, max_val))
    return merged



def sum_digits(file):
    lines = read_file(file)
    fresh = get_fresh_ranges(lines)
    _sum = 0
    for fresh_range in fresh:
        _sum += fresh_range[1] - fresh_range[0] + 1
    print(_sum)
    return _sum

assert 14 == sum_digits('test1.txt')
sum_digits('input.txt')
