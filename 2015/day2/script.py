

def wrapping_paper(file):
    with open(file, 'r') as fs:
        lines = fs.readlines()
    size = 0
    total_ribbon = 0
    for line in lines:
        line = line.rstrip('\n')
        sizes = line.split('x')
        l, w, h = (int(dim) for dim in sizes)
        lw = l * w
        wh = w * h
        hl = h * l
        surface = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(lw, wh, hl)
        size += (surface + slack)

        perim_lw = 2 * l + 2 * w
        perim_wh = 2 * w + 2 * h
        perim_hl = 2 * h + 2 * l
        ribbon = min(perim_wh, perim_hl, perim_lw)
        bow = l * w * h
        total_ribbon += (ribbon + bow)
    return (size, total_ribbon)


test_res = wrapping_paper('test.txt')
input_res =  wrapping_paper('input.txt')
assert 58 + 43 == test_res[0]
assert 34 + 14 == test_res[1]

print('Answer1: %s' % input_res[0])
print('Answer2: %s' % input_res[1])
